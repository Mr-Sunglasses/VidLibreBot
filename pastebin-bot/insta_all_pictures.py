import instaloader
from instaloader import Profile, Post
import shutil



def download_images_all(Username,Passoword,Insta_profile):
    instance = instaloader.Instaloader()

    instance.login(user=Username,passwd=Passoword)

    instance.download_profile(profile_name=Insta_profile)

def profile_delete_from_storage(Username):
    shutil.rmtree(f"{Username}")