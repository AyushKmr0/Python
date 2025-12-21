
import json

file_name = "youtube.txt"

def load_data():
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []    
    
def save_data_helper(videos):
    with open(file_name, 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print('\n', '*' * 50, '\n')
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print('\n', '*' * 50,'\n')

def add_video(videos):
    video_name = input("Enter video name: ")
    video_time = input("Enter video time: ")
    
    videos.append({'name': video_name, 'time': video_time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update "))

    if 1 <= index <= len(videos):
        video_name = input("Enter video name: ")
        video_time = input("Enter video time: ")
        
        videos[index - 1] = {'name': video_name, 'time': video_time}
        save_data_helper(videos)
    else:
        print("Invalid video index selected")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video to delete "))
    
    if 1 <= index <= len(videos):
        del videos[index - 1] 
        save_data_helper(videos)
    else:
        print("Invalid video index selected")

def main():
    videos = load_data()
    while True:
        print("\nYoutube Manager | choose an option")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")

        choice = input("\nEnter your choice ")
        
        match choice:
            case '1':
                list_all_videos(videos)
                
            case '2':
                add_video(videos)
            
            case '3':
                update_video(videos)
                
            case '4':
                delete_video(videos)
                
            case '5':
                break
            
            case _:
                print("Invalid Choice")
                
if __name__ ==  '__main__':
    main()
