
import json

def load_data():
    try:
        with open("youtube.txt","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos,file)

def list_videos(videos):
    for idex,value in enumerate(videos, start=1):
        print(f"{idex}")

def add_video(videos):
    name =input("Enter the name of the video: ")
    time = input("Enter time of the video: ")
    videos.append({"name": name,"time": time})
def update_video(videos):
    pass

def delete_video(videos):
    pass

def main():
    videos = load_data()
   

    while True:
        print("\n Youtube Manager  |  chose an option ")
        print("1. List all youtube videos")
        print("2. Add a Youtube video")
        print("3. Update a Youtube video details ")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("choose your choice: ")
        print(videos)

        match choice:
            case '1':
                list_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid enter a correct number ")
                
                
                
if __name__ == "__main__":
    main()


