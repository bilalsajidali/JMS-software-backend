from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from flask_jwt_extended import create_access_token
from database import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    password_hash = generate_password_hash(data['password'])
    new_user = {
        "name": data['name'],
        "email": data['email'],
        "password": password_hash,
        "created_at": "timestamp"
    }

    # Directly access the global db object
    result = db.users.insert_one(new_user)
    
    return jsonify({"message": "User created successfully", "user_id": str(result.inserted_id)}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    # Mock user validation
    data = request.json
    if data["email"] == "test@example.com" and data["password"] == "password":
        token = create_access_token(identity=data["email"])
        return jsonify(access_token=token)
    return {"message": "Invalid credentials"}, 401
