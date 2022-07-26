import instaloader
import os
ig = instaloader.Instaloader()
dp = input("Enter Insta username : ")

ig.download_profile(dp, profile_pic_only=True)


for root, subdirs, files in os.walk(dp):
    for file in files:
        if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg'):
            print(file)
             # print(os.path.join(root, file))

