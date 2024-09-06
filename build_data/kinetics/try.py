from pytubefix import YouTube

v = 'http://youtube.com/watch?v=-3B32lodo2M'

v2 = 'http://youtube.com/watch?v=2lAe1cqCOXo'

try:
    yt = YouTube(v2)
except Exception as e:
    print(e)

print("yt.title: ", yt.title)

print("yt.streams: ", yt.streams)

# video = yt.streams.filter(
#         progressive=True, subtype='mp4', resolution='360p').first()


