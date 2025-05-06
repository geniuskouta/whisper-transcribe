import shutil
from pathlib import Path

def setup_dist():
    dist_dir = Path("dist")
    dist_dir.mkdir(exist_ok=True)

    # Copy audio_chunks and result into dist
    for folder_name in ["audio_chunks", "result"]:
        src = Path(folder_name)
        dst = dist_dir / folder_name
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)

    # Convert .srt files to .txt in dist
    for srt_file in dist_dir.rglob("*.srt"):
        txt_file = srt_file.with_suffix(".txt")
        srt_file.rename(txt_file)

if __name__ == "__main__":
    setup_dist()
    print("Setup complete. Check the 'dist' folder.")
