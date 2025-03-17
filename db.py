import os
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGODB_URI")
mongo_client = MongoClient(MONGO_URI)
db = mongo_client["culinary_chat"]
collection = db["chat_history"]

def get_chat_history():
    return list(collection.find({}, {"_id": 0}))

def save_message(role: str, content: str):
    collection.insert_one({"role": role, "content": content})

try:
    mongo_client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
    db = mongo_client["culinary_chat"]
    collection = db["chat_history"]
    
    mongo_client.admin.command('ping')
    print("Successfully connected to MongoDB Atlas")
    
except Exception as e:
    print(f"MongoDB Connection Error: {e}")
    exit(1)