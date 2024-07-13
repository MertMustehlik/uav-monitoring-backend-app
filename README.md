# Web-based UAV Monitoring and Task Execution

This project is a web-based UAV (Unmanned Aerial Vehicle) monitoring and task execution application developed with Python Flask. The application allows users to manage UAV tasks and monitor UAVs in real-time.

## Installation

### 1. Create Database (mySql)

db_name = uav-task-app

```sh
python seed.py
```
### 2. Run Application

```sh
python run.py
```

Starts the application and runs it on http://localhost:5000.

## Technologies Used

- Flask
- Flask SQLAlchemy
- Flask CORS
- PyJWT
- Pillow (PIL)

## API Endpoints

The application provides RESTful API endpoints for managing UAV tasks and monitoring

### Authenticate

- `POST /api/auth/login`: User login authentication.
- `POST /api/auth/check`: Check authentication status.

### Drones

- `GET /api/drones`: List all drones.
- `POST /api/drones`: Create a new drone.

### Tasks

- `GET /api/tasks`: List all tasks.
- `GET /api/tasks/{id}`: Get details of a specific task.
- `POST /api/tasks`: Create a new task.
- `POST /api/tasks/{id}/execute`: Execute a specific task.
- `GET /api/tasks/{id}/images`: Retrieve images related to a specific task.
