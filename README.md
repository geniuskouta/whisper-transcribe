# Transcribe interview audio

The purpose is to transcribe speech in a video.

## Convert mp4 to mp3

```
python scripts/convert_to_mp3 <mp4_filename>
```

## Split the mp3 file into smaller files

*Whisper cannot take more than 20MB at once

```
python scripts/split_by_silence.py <mp3_filename>
```

## Transcribe the audio files

```
python scripts/transcribe_chunks.py
```

## Create dist folder to share with non programmers

```
python scripts/create_dist.py
```
