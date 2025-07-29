import os
import shutil
import time
import sys

def perceive(directory):
    return os.listdir(directory)

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

def run_agent(base_dir):
    print(f"[Polling Agent Started] Watching: {base_dir}")
    while True:
        files = perceive(base_dir)
        for file in files:
            if file in ['images', 'docs', 'others']:
                continue
            decision = decide(file)
            act(file, decision, base_dir)
            print(f"Moved '{file}' → '{decision}/'")
        time.sleep(2)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python polling_agent.py <folder_to_watch>")
        sys.exit(1)
    folder = sys.argv[1]
    if not os.path.exists(folder):
        print(f"Folder does not exist: {folder}")
        sys.exit(1)
    run_agent(folder)
