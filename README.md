# youtube_transcript
This code is a unit part of the major project. It uses whisper by openAI to retrieve accurate transcript from youtube video. The other libraries used are pytube, moviepyeditor.
It first extract the audio part of the video and uses AudioFileClip to handle the audio file(mp4 format)
After the extraction and modifying .mp4 to .wav we remove the clip we stored
We then transcribe using whisper's pre defined methods. Whisper model used here is base
