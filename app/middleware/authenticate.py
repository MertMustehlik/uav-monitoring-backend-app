from flask import jsonify, request
from functools import wraps
from app import SECRET_KEY
import jwt

def authenticate_middleware(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token or not token.startswith('Bearer '):
            return jsonify({'success': False, 'message': 'Unauthorized'}), 401

        jwt_token = token.split(' ')[1] 

        try:
            payload = jwt.decode(jwt_token, SECRET_KEY, algorithms=["HS256"])
            return func(*args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify({'success': False, 'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'success': False, 'message': 'Invalid token'}), 401

    return decorated