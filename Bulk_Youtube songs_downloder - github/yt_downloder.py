import os
import subprocess

INPUT_FILE = "songs.txt"
OUTPUT_DIR = "downloaded_songs"

def read_urls(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def download_audio(url):
    command = [
    "yt-dlp.exe",
    "--extract-audio",
    "--audio-format", "mp3",
    "--ffmpeg-location", ".",  # ⬅️ Tells yt-dlp to use ffmpeg from current folder
    "--output", f"{OUTPUT_DIR}/%(title)s.%(ext)s",
    url
]

    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"✅ Downloaded: {url}")
    else:
        print(f"❌ Failed: {url}\n{result.stderr}")

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    if not os.path.exists(INPUT_FILE):
        print(f"❌ File '{INPUT_FILE}' not found.")
        return

    urls = read_urls(INPUT_FILE)
    print(f"🎯 {len(urls)} songs found.")

    for url in urls:
        download_audio(url)

    print("\n🎉 Done! Check your 'downloaded_songs' folder.")

if __name__ == "__main__":
    main()
