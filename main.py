import pytube 
from moviepy.editor import VideoFileClip
import pywhisper
import os
import sys
# import static_ffmpeg
# https://github.com/openai/whisper

def download_video(url):
    print("Downloading Video...")
    video = pytube.YouTube(url)
    stream = video.streams.get_by_itag(18)
    stream.download()
    return stream.default_filename

def convert_to_mp3(filename):
    print("Extracting Audio...")
    clip = VideoFileClip(filename)
    name = filename[:-4]+ ".mp3"
    clip.audio.write_audiofile(name)
    clip.close()
    return name

def AudiotoText(filename):
    print("Transcribing...")
    model = pywhisper.load_model("base")
    result = model.transcribe(filename)
    text = result["text"]
    return text


def main(url, destination):
    # print("Initializing FFMPEG...")
    # static_ffmpeg.add_paths()
    videoFile = download_video(url)
    mp3File = convert_to_mp3(videoFile)
    result = AudiotoText(mp3File)
    
    with open(destination, 'w') as f:
        f.write(result)
        f.close()

    os.unlink(videoFile)
    os.unlink(mp3File)


if __name__ == "__main__":
    video = sys.argv[1]
    destination = sys.argv[2]
    main(video, destination)