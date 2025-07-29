import os
import shutil
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def decide(file):
    if file.endswith(('.jpg', '.png')):
        return 'images'
    elif file.endswith(('.pdf', '.txt', '.docx')):
        return 'docs'
    else:
        return 'others'

def act(file, decision, base_dir):
    dest = os.path.join(base_dir, decision)
    os.makedirs(dest, exist_ok=True)
    shutil.move(os.path.join(base_dir, file), os.path.join(dest, file))

class Handler(FileSystemEventHandler):
    def __init__(self, base_dir):
        self.base_dir = base_dir

    def on_created(self, event):
        if event.is_directory:
            return
        file = os.path.basename(event.src_path)
        if file in ['images', 'docs', 'others']:
            return
        decision = decide(file)
        act(file, decision, self.base_dir)
        print(f"Moved '{file}' → '{decision}/'")

def run_agent(base_dir):
    print(f"[Event Agent Started] Watching: {base_dir}")
    observer = Observer()
    event_handler = Handler(base_dir)
    observer.schedule(event_handler, path=base_dir, recursive=False)
    observer.start()
    observer.join()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python event_agent.py <folder_to_watch>")
        sys.exit(1)
    folder = sys.argv[1]
    if not os.path.exists(folder):
        print(f"Folder does not exist: {folder}")
        sys.exit(1)
    run_agent(folder)
