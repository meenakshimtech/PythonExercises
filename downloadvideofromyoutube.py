from pytube import YouTube
SAVE_PATH = "D:/foldername"
link = "https://www.youtube.com/watch?v=XXXXXXX"
yt = YouTube(link)
stream = yt.streams.first()
stream.download(SAVE_PATH)
