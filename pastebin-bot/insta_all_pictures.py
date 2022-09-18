from instaloader import Instaloader,Profile
import threading
import shutil

profile_instance = Instaloader()


def fetch_posts(user):

    try:
        prof = Profile.from_username(profile_instance.context, user)
        print(prof)
        posts = prof.get_posts()
    except:
        raise FileNotFoundError
    

    for post in posts:
        try:
            task = threading.Thread(target=profile_instance.download_post, args=(post,user,))
            task.start()
        except:
            print("Skipping due to status code 401")


def profile_delete(username):
    shutil.rmtree(f"{username}")
