import instaloader
import os
import shutil


def profile_downloader(username):
    ig = instaloader.Instaloader()
    ig.download_profile(username, profile_pic_only=True)


# dp = input("Enter Insta username : ")

def profile_delete(username):
    shutil.rmtree(f'{username}')



