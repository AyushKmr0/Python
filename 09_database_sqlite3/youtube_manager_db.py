import sqlite3

DB_NAME = "youtube_vidoes.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_table():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS videos (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL,
                           duration TEXT NOT NULL
                       )
                       ''')

def execute_query(query, params=(), fetch=False):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        
        if fetch:
            return cursor.fetchall()

def list_videos():
    videos = execute_query("SELECT * FROM videos", fetch=True)

    if not videos:
        print("\nNo video found.")
        return
    
    print("\n", '*'*50, '\n')
    for vid in videos:
        print(f"ID: {vid[0]} |  Name: {vid[1]} | Duration: {vid[2]}")
        
    print("\n", '*'*50, '\n')
        
def add_video(name, duration):
    if not name:
        print("\nVideo name cannot be empty.")
        return
    
    execute_query("INSERT INTO videos (name, duration) VALUES (?, ?)", (name, duration))
    
    print("\nVideo added successfully!")

def update_video(video_id, new_name, new_duration):
    execute_query("UPDATE videos SET name=?, duration=? WHERE id=?", (new_name, new_duration, video_id))
    
    print("\nVideo updated (if ID existed).")

def delete_video(video_id):
    execute_query("DELETE FROM videos WHERE id=?", (video_id,))
    
    print("\nVideo deleted (if ID existed).")
        
def main():
    create_table()
    
    while True:
        print("\nYOUTUBE VIDEO MANAGER")
        print("1. List videos")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()
        
        try:
            if choice == '1':
                list_videos()
                
            elif choice == '2':
                name = input("Video name: ").strip()
                duration = input("Vidoe duration: ").strip()
                
                add_video(name, duration)
                
            elif choice == '3':
                video_id = int(input("Enter video ID: ").strip())
                name = input("Video name: ").strip()
                duration = input("Vidoe duration: ").strip()
                
                update_video(video_id, name, duration)
                
            elif choice == '4':
                video_id = int(input("Enter video ID: ").strip())
                
                delete_video(video_id)
                
            elif choice == '5':
                break
            
            else:
                print("Invalid choice!")                
        
        except ValueError:
            print("Please enter a valid number.")
        except sqlite3.Error as e:
            print("Database error:", e)
            

if __name__ == '__main__':
    main()
