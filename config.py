import os

# MongoDB configuration
MONGO_URI = "mongodb://localhost:27017/task_manager_db"  # MongoDB will create 'task_manager_db' on first data insert
SECRET_KEY = os.urandom(24)  # Used for session management
