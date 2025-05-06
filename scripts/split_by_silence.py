import sys
from pathlib import Path
from pydub import AudioSegment
from pydub.silence import split_on_silence

def normalize_audio(audio, target_dBFS=-20.0):
    change_in_dBFS = target_dBFS - audio.dBFS
    return audio.apply_gain(change_in_dBFS)

def split_audio(file_path):
    file_path = Path(file_path)
    print(f"Loading {file_path}...")
    audio = AudioSegment.from_file(file_path)
    print(f"Original dBFS: {audio.dBFS:.2f}")

    normalized_audio = normalize_audio(audio)
    print(f"Normalized dBFS: {normalized_audio.dBFS:.2f}")

    print("Splitting on silence...")
    chunks = split_on_silence(
        normalized_audio,
        min_silence_len=2000,
        silence_thresh=normalized_audio.dBFS - 16,
        keep_silence=500
    )

    output_dir_path = Path("audio_chunks")
    output_dir_path.mkdir(parents=True, exist_ok=True)

    for i, chunk in enumerate(chunks):
        out_path = output_dir_path / f"chunk_{i:03d}.mp3"
        print(f"Exporting {out_path}")
        chunk.export(out_path, format="mp3")

    print(f"Done. {len(chunks)} chunks saved to {output_dir_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python split_by_silence.py audio/your_audio.mp3")
        sys.exit(1)

    split_audio(sys.argv[1])
