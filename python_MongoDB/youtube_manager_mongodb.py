from pymongo import MongoClient

client = MongoClient("")

db = client["youtube_manager"]
video_collection = db["videos"]