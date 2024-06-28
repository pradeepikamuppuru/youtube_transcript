import whisper
from pytube import YouTube
import os
from moviepy.editor import AudioFileClip

model = whisper.load_model("base")

def download_youtube_video_as_audio(youtube_url, output_path='audio.wav'):
    try:
        yt = YouTube(youtube_url)
        video = yt.streams.filter(only_audio=True).first()
        output_file = video.download(filename='temp.mp4')
        audio_clip = AudioFileClip(output_file)
        audio_clip.write_audiofile(output_path, codec='pcm_s16le')
        audio_clip.close()
        os.remove(output_file)
        return output_path
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def transcribe_audio(audio_path):
        result = model.transcribe(audio_path)
        return result['text']
    


youtube_url = input("Enter YouTube URL: ")
audio_path = download_youtube_video_as_audio(youtube_url)
if audio_path:
    transcript = transcribe_audio(audio_path)
    print("Transcription: ")
    print(transcript)
os.remove(audio_path)
