import whisper
import os
from pathlib import Path

def transcribe_audio(chunk_file_path, model, result_dir):
    print(f"Transcribing {chunk_file_path}...")

    result = model.transcribe(str(chunk_file_path), verbose=False, task="transcribe")

    # Prepare result dir
    result_dir.mkdir(parents=True, exist_ok=True)
    
    # Save .srt file
    srt_file_path = result_dir / (chunk_file_path.stem + '.srt')
    with open(srt_file_path, 'w', encoding='utf-8') as f:
        for i, segment in enumerate(result['segments'], 1):
            start = format_timestamp(segment['start'])
            end = format_timestamp(segment['end'])
            f.write(f"{i}\n{start} --> {end}\n{segment['text'].strip()}\n\n")

    print(f"SRT saved to {srt_file_path}")

def format_timestamp(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds - int(seconds)) * 1000)
    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"

def transcribe_chunks_in_directory(directory_path, result_dir):
    model = whisper.load_model("medium")  # You can change to "medium" or "large"
    chunk_files = sorted(Path(directory_path).glob("*.mp3"))  # Ensure ordered processing
    for chunk_file in chunk_files:
        transcribe_audio(chunk_file, model, result_dir)

if __name__ == "__main__":
    directory_path = "audio_chunks"
    result_dir = Path("result")
    transcribe_chunks_in_directory(directory_path, result_dir)
