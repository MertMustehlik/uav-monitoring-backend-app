from flask import Blueprint, request, jsonify
from app.models import Drone
from app import db
from functools import wraps
from app.middleware.authenticate import authenticate_middleware


module = Blueprint('drones', __name__)

def drone_to_format(drone):
    return {
        'id': drone.id,
        'name': drone.name,
        'created_at': drone.created_at,
        'tasks': [{"id": task.id, "name": task.name, "description": task.description, "start_at": format(task.execute_at)} for task in drone.tasks] if hasattr(drone, 'tasks') else []
    }

@module.route('/', methods=['GET'])
@authenticate_middleware
def index():
    drones = Drone.query.order_by(Drone.id.desc()).all()

    drones_list = [drone_to_format(drone) for drone in drones]
    return jsonify({"success": True, "payload": drones_list})

@module.route('/', methods=['POST'])
@authenticate_middleware
def create():
    name = request.form.get("name")
    if not name:
        return jsonify({"success": False, "message": "name is required"}), 400

    try:
        new_drone = Drone(name=name)
        db.session.add(new_drone)
        db.session.commit()

        return jsonify({"success": True, "message": "Drone created successfully", "payload": drone_to_format(new_drone)}), 201
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500