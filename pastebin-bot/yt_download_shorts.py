# import pafy
# import youtube_dl
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
#
# def download_video(link_of_video):
#     link = link_of_video
#     video = pafy.new(link)
#     best = video.getbest()
#     best.download()
#
# def get_title(link_of_video):
#     link = link_of_video
#     video = pafy.new(link)
#     best = video.getbest()
#     return best.title

from pytube import YouTube

def download_video(link_of_video):
    url = link_of_video

    myvideo = YouTube(url)

    download = myvideo.streams.get_by_resolution()

    download.download()

def get_title(link_of_video):
    url = link_of_video

    myvideo = YouTube(url)

    return myvideo.title
