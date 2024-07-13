from flask import Blueprint, request, jsonify
from app import db
from app.models.user import User
import datetime
import jwt
from werkzeug.security import check_password_hash
from app.middleware.authenticate import authenticate_middleware
from app import SECRET_KEY

module = Blueprint('auth', __name__)

@module.route('/login', methods=['POST'])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    if not email or not password:
        return jsonify({"success": False, "message": "email and password is required"}), 400

    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({"success": False, "message": "Invalid email or password"}), 401

    if check_password_hash(user.password, password):
        jwt_token = jwt.encode({
            'email': user.email,
            'exp': datetime.datetime.now() + datetime.timedelta(minutes=30)
        }, SECRET_KEY)

        return jsonify({"success": True, "message": "Login successful", "token": jwt_token}), 200
    else:
        return jsonify({"success": False, "message": "Invalid email or password"}), 401
    
@module.route('/check', methods=['POST'])
@authenticate_middleware
def authCheck():
    token = request.headers.get('Authorization')
    jwt_token = token.split(' ')[1] 
    
    return jsonify({"success": True, "message": "Logged in", "token": jwt_token}), 200