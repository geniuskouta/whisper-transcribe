import subprocess
import sys
from pathlib import Path

def convert_to_mp3(input_path: str, output_path: str = None):
    input_file = Path(input_path)
    if not input_file.exists():
        raise FileNotFoundError(f"{input_file} not found.")

    output_file = Path(output_path) if output_path else input_file.with_suffix(".mp3")

    command = [
        "ffmpeg",
        "-i", str(input_file),
        "-vn",  # no video
        "-acodec", "libmp3lame",
        "-q:a", "2",  # quality (2 is high)
        str(output_file)
    ]

    print("Running:", " ".join(command))
    subprocess.run(command, check=True)
    print(f"Saved MP3 to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_to_mp3.py <input_video>")
        sys.exit(1)

    convert_to_mp3(sys.argv[1])
