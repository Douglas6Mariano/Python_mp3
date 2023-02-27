import os

from pytube import YouTube

yt = YouTube ('https://www.youtube.com/watch?v=t050lriI0_w')   #ULR do youtube

video = yt.streams.filter(only_audio=True).first()

download_file = video.download()
base, ext = os.path.splitext(download_file)

new_file = base + '.mp3'
os.rename(download_file, new_file)

print('Download Concluido....')