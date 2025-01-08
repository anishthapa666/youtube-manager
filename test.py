import json

def load_data():
    try:
        with open("youtube.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)

def list_videos(videos):
    print("\n")
    print("-" * 69)
    for index, video in enumerate(videos, start=1):
        print(f"{index}) {video['name']}, duration is {video['time']}")
    print("-" * 69)

def add_video(videos):
    name = input("Enter the name of the video: ")
    time = input("Enter the time of the video: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)

def update_video(videos):
    list_videos(videos)
    try:
        index = int(input("Choose the video you want to update: "))
        if 1 <= index <= len(videos):
            name = input("Enter the new name of the video: ")
            time = input("Enter the new time of the video: ")
            videos[index - 1] = {"name": name, "time": time}
            save_data_helper(videos)
        else:
            print("Invalid index")
    except ValueError:
        print("Please enter a valid number.")

def delete_video(videos):
    list_videos(videos)
    try:
        index = int(input("Enter the video number you want to delete: "))
        if 1 <= index <= len(videos):
            del videos[index - 1]
            save_data_helper(videos)
        else:
            print("Invalid index")
    except ValueError:
        print("Please enter a valid number.")

def main():
    videos = load_data()

    while True:
        print("\nYoutube Manager  |  Choose an option")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update YouTube video details")
        print("4. Delete a YouTube video")
        print("5. Exit the app")
        choice = input("Choose your choice: ")

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
                print("Invalid choice. Please enter a correct number.")

if __name__ == "__main__":
    main()
