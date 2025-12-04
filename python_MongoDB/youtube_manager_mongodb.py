from pymongo import MongoClient

client = MongoClient("")

db = client["youtube_manager"]
video_collection = db["videos"]

print(video_collection)

def main():
    while True:
        print("\n YouTube Manager")
        print("1. List all youtube videos")
        print("2. Add a new youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice (1-5): ")
        

if __name__ == "__main__":
    main()