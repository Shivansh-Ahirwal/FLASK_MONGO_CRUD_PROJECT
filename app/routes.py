from flask import Blueprint, jsonify, request
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from .database import mongo 

main = Blueprint("main", __name__)


def serialize_user(user):
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "password": user["password"] 
    }

@main.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    return jsonify([serialize_user(user) for user in users])

@main.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = mongo.db.users.find_one({"_id": ObjectId(id)})
    if user:
        return jsonify(serialize_user(user))
    else:
        return jsonify({"error": "User not found"}), 404

@main.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    hashed_password = generate_password_hash(data.get("password"))

    user_id = mongo.db.users.insert_one({
        "name": data.get("name"),
        "email": data.get("email"),
        "password": hashed_password
    }).inserted_id

    return jsonify({"id": str(user_id)}), 201

@main.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    user = mongo.db.users.find_one({"_id": ObjectId(id)})

    if user:
        updated_data = {}
        if "name" in data:
            updated_data["name"] = data["name"]
        if "email" in data:
            updated_data["email"] = data["email"]
        if "password" in data:
            updated_data["password"] = generate_password_hash(data["password"])

        mongo.db.users.update_one({"_id": ObjectId(id)}, {"$set": updated_data})
        return jsonify({"message": "User updated successfully"})
    else:
        return jsonify({"error": "User not found"}), 404


@main.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    result = mongo.db.users.delete_one({"_id": ObjectId(id)})
    if result.deleted_count:
        return jsonify({"message": "User deleted successfully"})
    else:
        return jsonify({"error": "User not found"}), 404
