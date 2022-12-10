import pytube 
from moviepy.editor import VideoFileClip
import pywhisper
import os
# import static_ffmpeg

# https://github.com/openai/whisper

def download_video(url):
    video = pytube.YouTube(url)
    stream = video.streams.get_by_itag(18)
    stream.download()
    return stream.default_filename

def convert_to_mp3(filename):
    clip = VideoFileClip(filename)
    name = filename[:-4]+ ".mp3"
    clip.audio.write_audiofile(name)
    clip.close()
    return name

def AudiotoText(filename):
    print("Transcribing...")
    model = pywhisper.load_model("tiny")
    result = model.transcribe(filename)
    sonuc = result["text"]
    return sonuc


def main(url):
    print("Initializing FFMPEG...")
    # static_ffmpeg.add_paths()
    fileName = download_video(url)
    mp3File = convert_to_mp3(fileName)
    result = AudiotoText(mp3File)
    print(result)

if __name__ == "__main__":
    main('https://www.youtube.com/watch?v=WHoWGNQRXb0')