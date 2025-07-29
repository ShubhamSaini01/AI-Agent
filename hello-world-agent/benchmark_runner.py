import os
import time
import shutil
from pathlib import Path

# === CONFIGURABLE PARAMS ===
NUM_FILES = 100
TEST_DIR = Path("test_files")
FILE_TYPES = ['.jpg', '.pdf', '.zip']
LOG_FILE = "benchmark_results.log"

def create_test_dir():
    if TEST_DIR.exists():
        shutil.rmtree(TEST_DIR)
    TEST_DIR.mkdir(parents=True)

def generate_test_files():
    for i in range(NUM_FILES):
        ext = FILE_TYPES[i % len(FILE_TYPES)]
        file_path = TEST_DIR / f"file_{i:03d}{ext}"
        with open(file_path, 'w') as f:
            f.write("dummy content\n")

def log(msg):
    with open(LOG_FILE, 'a') as f:
        f.write(msg + "\n")
    print(msg)

def wait_for_processing(timeout=30):
    start_time = time.time()
    while time.time() - start_time < timeout:
        total_processed = 0
        for subdir in ['images', 'docs', 'others']:
            sub_path = TEST_DIR / subdir
            if sub_path.exists():
                total_processed += len(os.listdir(sub_path))
        if total_processed >= NUM_FILES:
            break
        time.sleep(0.5)
    return time.time() - start_time

def main():
    log("=== Benchmark Start ===")
    create_test_dir()
    generate_test_files()
    log(f"Generated {NUM_FILES} test files.")

    input("⚠️ Start your agent in another terminal, then press Enter to begin benchmark...")

    log("⏱ Measuring processing time...")
    duration = wait_for_processing(timeout=30)
    log(f"✅ All files processed in {duration:.2f} seconds.")
    log("=== Benchmark End ===\n")

if __name__ == "__main__":
    main()

