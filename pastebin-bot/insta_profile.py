import instaloader
import os
import shutil
from dotenv import load_dotenv

load_dotenv()


def profile_downloader(username):
    name = os.getenv('username')
    passw = os.getenv('password')
    ig = instaloader.Instaloader()
    ig.login(name, passw)
    ig.download_profile(username, profile_pic_only=True)


# dp = input("Enter Insta username : ")
def get_all_images(username):
    name = os.getenv('username')
    passw = os.getenv('password')
    ig = instaloader.Instaloader()
    ig.login(name, passw)



def profile_delete(username):
    shutil.rmtree(f'{username}')
