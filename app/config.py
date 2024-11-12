import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecret')
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://mongo:27017/flask_db')
