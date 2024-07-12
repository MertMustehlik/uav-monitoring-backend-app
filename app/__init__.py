from flask import Flask, send_file
from flask_sqlalchemy import SQLAlchemy
from config import configuration
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.config.update(configuration.__dict__)


db = SQLAlchemy(app)

from app.controllers.drone_controller import module as drones_module
from app.controllers.task_controller import module as tasks_module

app.register_blueprint(drones_module, url_prefix='/api/drones')
app.register_blueprint(tasks_module, url_prefix='/api/tasks')

@app.route('/api/uploads/<filename>', methods=['GET'])
def uploaded_file(filename):
    file_path = "uploads/" + filename 
    return send_file(file_path)

from app.models import drone, task, image