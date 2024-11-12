from bson import ObjectId
from app import mongo

def user_schema(data):
    """Schema for formatting user data."""
    return {
        "id": str(data.get("_id", "")),
        "name": data.get("name", ""),
        "email": data.get("email", "")
    }
