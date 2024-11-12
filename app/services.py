from werkzeug.security import generate_password_hash, check_password_hash
from app import mongo
from bson import ObjectId
from models import user_schema

def create_user(data):
    data["password"] = generate_password_hash(data["password"])
    user_id = mongo.db.users.insert_one(data).inserted_id
    return str(user_id)

def get_all_users():
    return [user_schema(user) for user in mongo.db.users.find()]

def get_user_by_id(user_id):
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    return user_schema(user) if user else None

def update_user(user_id, data):
    if "password" in data:
        data["password"] = generate_password_hash(data["password"])
    mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": data})

def delete_user(user_id):
    mongo.db.users.delete_one({"_id": ObjectId(user_id)})
