import time

from API import API_KEY
import telebot
import os, subprocess, threading
from request import file_writer, file_remover
from insta_profile import profile_downloader, profile_delete
from insta_all_pictures import fetch_posts, profile_delete
from qr_generator import generate_qr, delete_qr
from quotes import preload_quotes, quotes
from random import randint
from love_quotes import happy_love_quotes, sad_love_quotes
from yt_download_shorts import download_video, get_title
import instaloader
from link_shortner import short

bot = telebot.TeleBot(API_KEY)

# TBD
# def handle_message(update, context):
#     user_first_name = update.message.chat.first_name
#     user_last_name = update.message.chat.last_name
#     username = update.message.chat.username
#     update.message.reply_text(
#         f"Hey👋 {user_first_name} {user_last_name} aka @{username} welcome to the Open-Bot type: /help to explore options."
#     )
#
#


# This Decorator handle's the message with and /start
@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.reply_to(
        message,
        "Welcome to Open-Bot Powered by Open-Source and Developed by @thisiskanishkP",
    )
    bot.send_photo(chat_id=message.chat.id, photo=open("images/octocat.png", "rb"))


# This Decorator helps in handling the message with /help
@bot.message_handler(commands=["help"])
def handle_help(message):
    bot.reply_to(
        message,
        """\
    The Following Commands can we user

     /start - to say welcome message
     /help - to get help
     /paste <content> - to push content to paste.rs
     /pic <insta user name> - to download a profile pic of the user
     /post <insta user name> - to download all pictures posted by the user
     /qr <link of data> - to generate qr code
     /quote - for getting random quotes
     /love_quote_happy - for romantic quotes [happy]
     /love_quote_sad - for romantic quotes [sad]
     /yt_dl <link of youtube video> - to download a youtube video.......[it may take sometime to download a youtube video so chill]
     /short <link> - To shorten the link\
    """,
    )


# This Decorator helps in handling the message with /paste
@bot.message_handler(commands=["paste"])
def handle_paste(message):
    chat_id = message.chat.id
    data = message.text
    send_data = data[7::]
    file_writer(text=send_data)
    output = subprocess.check_output(
        "curl --data-binary @file.txt https://paste.rs/", shell=True
    )
    bot.send_message(chat_id, f"{output.decode('utf-8')}")
    file_remover()


# This Decorator helps in handling the message with /pic
@bot.message_handler(commands=["pic"])
def handle_pic(message):
    chat_id = message.chat.id
    data = message.text
    username = data[5::]
    print(username)
    try:
        profile_downloader(username=username)
        bot.reply_to(
            message,
            f"Please wait while we are sending you the profile pic of {username} \n Don't worry it will take a minute or so 🤝",
        )
        for root, subdirs, files in os.walk(username):
            for file in files:
                if os.path.splitext(file)[1].lower() in (".jpg", ".jpeg"):
                    bot.send_photo(
                        chat_id, photo=open(f"{os.path.join(root, file)}", "rb")
                    )
                    profile_delete(username=username)
    except:
        bot.reply_to(message, f"{username} is not found")


# This Decorator helps in handling the message with /post
@bot.message_handler(commands=["post"])
def handle_insta(message):
    chat_id = message.chat.id
    data = message.text
    username = data[6::]
    try:
        task = threading.Thread(target=fetch_posts, args=(username,))
        task.start()
        bot.reply_to(
            message, f"Getting posts of {username} for you. \nPlease wait for a moment."
        )
        task.join()
        for root, subdirs, files in os.walk(username, topdown=False):
            for file in files:
                if os.path.splitext(file)[1].lower() in (".jpg", ".jpeg"):
                    bot.send_photo(
                        chat_id, photo=open(f"{os.path.join(root, file)}", "rb")
                    )

        profile_delete(username=username)

    except FileNotFoundError:
        bot.reply_to(message, f"{username} is not found")


# This Decorator helps in handling the message with /qr
@bot.message_handler(commands=["qr"])
def handle_qr(message):
    chat_id = message.chat.id
    text = message.text
    link = text[4::]
    try:
        generate_qr(link=link)
        bot.send_photo(chat_id=chat_id, photo=open("myqr.png", "rb"))
        delete_qr()
    except:
        bot.reply_to(message, f"QR of this {link} can't be generated")
        delete_qr()


# This Decorator helps in handling the message with /quote
@bot.message_handler(commands=["quote"])
def handle_quote(message):
    chat_id = message.chat.id
    preload_quotes()
    bot.reply_to(message, f"{quotes[0]}")


# This Decorator helps in handling the message with /love_quote_happy
@bot.message_handler(commands=["love_quote_happy"])
def handle_love_quote_happy(message):
    bot.reply_to(message, f"❤️ {happy_love_quotes[randint(0, 22)]}")


# This Decorator helps in handling the message with /love_quote_sad
@bot.message_handler(commands=["love_quote_sad"])
def handle_love_quote_sad(message):
    bot.reply_to(message, f"❤️ {sad_love_quotes[randint(0, 22)]}")


# This Decorator helps in handling the message with /yt_dl
@bot.message_handler(commands=["yt_dl"])
def handle_video_download_yt(message):
    chat_id = message.chat.id
    data = message.text
    link_video = data[7::]
    try:
        bot.send_message(
            chat_id,
            "Please wait while the Video is Downloading, It may take 3-5 minutes to download a 20 mb video 🙏",
        )
        download_video(link_video)
        bot.send_video(chat_id, video=open("output.mp4", "rb"), supports_streaming=True)
        time.sleep(
            50
        )  # Alternate way, the problem occurs when file deletion, Better way to use Async await for this task
        if os.path.exists("output.mp4"):
            os.remove("output.mp4")
    except instaloader.ProfileNotExistsException:
        bot.reply_to(message, f"{link_video} is not Found")
    except instaloader.ConnectionException:
        bot.reply_to(message, "IP is Blocked Please Try After Some Time")


# This Decorator Deals with /short
@bot.message_handler(commands=["short"])
def handle_short(message):
    chat_id = message.chat.id
    data = message.text
    payload_link_data = data[7::]
    try:
        bot.reply_to(message, f"{short(payload_link_data)}")
    except:
        bot.reply_to(message, f"We can't abel to short{payload_link_data}")


if __name__ == "__main__":
    bot.infinity_polling()
