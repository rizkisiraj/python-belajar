import pytube

yt = pytube.YouTube('https://www.youtube.com/watch?v=MYdoV6LLL9A&ab_channel=FreeNoCopyright-Instrumentals%2CBeats%2CMusic')

streams = yt.streams.filter(only_audio=True)
streams = yt.streams.get_by_itag(140)

streams.download()