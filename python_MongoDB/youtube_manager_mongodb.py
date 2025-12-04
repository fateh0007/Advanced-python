from pymongo import MongoClient

client = MongoClient("")

db = client["youtube_manager"]
video_collection = db["videos"]

print(video_collection)

def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")

def add_video(name, time): 
    video_collection.insert_one({"name": name, "time": time})

def update_video(video_id, name, time):
    video_collection.update_one(
        {'_id': video_id},
        {"$set": {'name': name, 'time': time}}
    )

def delete_video(video_id):
    video_collection.delete_one({'_id': video_id})

def main():
    while True:
        print("\n YouTube Manager")
        print("1. List all youtube videos")
        print("2. Add a new youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter the ID of the video to update: ")
            name = input("Enter the new name of the video: ")
            time = input("Enter the new time of the video: ")
            update_video(video_id,name, time)
        elif choice == '4':
            video_id = input("Enter the ID of the video to delete: ")
            delete_video(video_id)
        else:
            break
            
if __name__ == "__main__":
    main()