from flask import Blueprint, request, jsonify
from app.models import Drone
from app import db
from datetime import datetime
from PIL import Image as PILImage, ImageDraw
import random
import os

module = Blueprint('tasks', __name__)

from app.models.task import Task
from app.models.drone import Drone
from app.models.image import Image


def task_to_format(task):
    return {
        'id': task.id,
        'name': task.name,
        'description': task.description,
        'execute_at': task.execute_at,
        'drone': {
            'id': task.drone.id,
            'name': task.drone.name,
            'created_at': task.drone.created_at
        }
    }

def image_to_format(image):
    return {
        'id': image.id,
        'path': image.path
    }

@module.route('/', methods=['GET'])
def index():
    tasks = Task.query.order_by(Task.id.desc()).all()
    tasks_list = [task_to_format(task) for task in tasks]

    return jsonify({"success": True, "payload": tasks_list}), 200

@module.route('/', methods=['POST'])
def create():
    name = request.form.get("name")
    description = request.form.get("description")
    drone_id = request.form.get("drone_id")
    if not name:
        return jsonify({"success": False, "message": "name is required"}), 400

    try:
        drone = Drone.query.get(drone_id)
        if not drone:
            return jsonify({"success": False, "message": "Drone not found"}), 404
        new_task = Task(name=name, description=description, drone_id=drone_id)

        db.session.add(new_task)
        db.session.commit()

        return jsonify({"success": True, "message": "Task created successfully", "payload": task_to_format(new_task)}), 201
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500
    
@module.route('/<int:id>', methods=['GET'])
def show(id):
    task = Task.query.get(id)
    if not task:
        return jsonify({"success": False, "message": "Task not found"}), 404

    return jsonify({"success": True, "payload": task_to_format(task)}), 200

@module.route('/<int:id>/execute', methods=['POST'])
def execute(id):
    try:
        task = Task.query.get(id)
        if not task:
            return jsonify({"success": False, "message": "Task not found"}), 404

        if task.execute_at:
           return jsonify({"success": False, "message": "Task has already been started on " + format(task.execute_at)}), 400
        
        task.execute_at = datetime.now()
  
        for i in range(5):
            img = PILImage.new('RGB', (300, 300), color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

            random_number = random.randint(100000, 999999)

            image_name = f"{i}_random_image_{random_number}.png"

            img_path = os.path.join('app/uploads', image_name)
            img.save(img_path)

            new_image = Image(path=image_name, task_id=task.id)
            db.session.add(new_image)

        db.session.commit()
        return jsonify({"success": True, "message": "Task successfully started", "payload": task_to_format(task)}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@module.route('/<int:id>/images', methods=['GET'])
def images(id): 
    try:
        task = Task.query.get(id)
        if not task:
            return jsonify({"success": False, "message": "Task not found"}), 404
    
        images = task.images 
        images_list = [image_to_format(image) for image in images]

        return jsonify({"success": True, "payload": images_list}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


