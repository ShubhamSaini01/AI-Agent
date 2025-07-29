import os
import shutil
import sys
import time
from dotenv import load_dotenv

load_dotenv()

USE_OPENAI = os.getenv("USE_OPENAI", "0") == "0"
USE_GEMINI = os.getenv("USE_GEMINI", "1") == "1"

# ==== Gemini Setup ====
if USE_GEMINI:
    from google import generativeai as genai
    gemini_key = os.getenv("AIzaSyA1xRG5eVBJrs3zgSz5Oj0bHa_LIyeD_LU")
    project_id = os.getenv("gen-lang-client-0321644476")
    client = genai.GenerativeModel(model_name="gemini-1.5-flash"        )


# ==== OpenAI Setup ====
if USE_OPENAI:
    import openai
    openai.api_key = os.getenv("OPENAI_API_KEY")

def decide(file_name):
    prompt = f"Decide the folder for this file: '{file_name}'. Choose from [images, docs, others]."

    if USE_GEMINI:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = client.generate_content(prompt)
        folder = response.text.strip().lower()
        print(f"[Gemini] {file_name} → {folder}")
        return folder

    elif USE_OPENAI:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        folder = response['choices'][0]['message']['content'].strip().lower()
        print(f"[OpenAI] {file_name} → {folder}")
        return folder

    else:
        print("[Error] No LLM provider enabled.")
        sys.exit(1)

def act(file, decision, base_dir):
    dest = os.path.join(base_dir, decision)
    os.makedirs(dest, exist_ok=True)
    shutil.move(os.path.join(base_dir, file), os.path.join(dest, file))

def run_agent(base_dir):
    print(f"[LLM Agent Started] Watching: {base_dir}")
    while True:
        files = os.listdir(base_dir)
        for file in files:
            if file in ['images', 'docs', 'others']:
                continue
            decision = decide(file)
            act(file, decision, base_dir)
        time.sleep(2)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python llm_agent.py <folder_to_watch>")
        sys.exit(1)
    folder = sys.argv[1]
    if not os.path.exists(folder):
        print(f"Folder does not exist: {folder}")
        sys.exit(1)
    run_agent(folder)

