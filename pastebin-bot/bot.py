from API import API_KEY
import telebot
import os, subprocess
from request import file_writer, file_remover
from insta_profile import profile_downloader, profile_delete
from qr_generator import generate_qr, delete_qr
from quotes import preload_quotes, quotes
from random import randint
from love_quotes import happy_love_quotes, sad_love_quotes
from yt_download_shorts import download_video, get_title
import instaloader

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
     /qr <link of data> - to generate qr code
     /quote - for getting random quotes
     /love_quote_happy - for romantic quotes [happy]
     /love_quote_sad - for romantic quotes [sad]
     /yt_dl <link of youtube video> - to download a youtube video.......[it may take sometime to download a youtube video so chill]\
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


@bot.message_handler(commands=["quote"])
def handle_quote(message):
    chat_id = message.chat.id
    preload_quotes()
    bot.reply_to(message, f"{quotes[randint(0, 9)]}")


@bot.message_handler(commands=["love_quote_happy"])
def handle_love_quote_happy(message):
    bot.reply_to(message, f"❤️ {happy_love_quotes[randint(0, 22)]}")


@bot.message_handler(commands=["love_quote_sad"])
def handle_love_quote_sad(message):
    bot.reply_to(message, f"❤️ {sad_love_quotes[randint(0, 22)]}")


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
        bot.send_video(
            chat_id, video=open(f"output.mp4", "rb"), supports_streaming=True
        )
        if os.path.exists(f"output.mp4"):
            os.remove(f"output.mp4")
    except instaloader.ProfileNotExistsException:
        bot.reply_to(message, f"{link_video} is not Found")
    except instaloader.ConnectionException:
        bot.reply_to(message, "IP is Blocked Please Try After Some Time")


# def video_download_yt(update, context):
#     link_video = context.args[0]
#     try:
#         update.message.reply_text(
#             "Please wait while the Video is Downloading, It may take 3-5 minutes to download a 20 mb video 🙏"
#         )
#         download_video(link_video)
#         context.bot.send_video(
#             chat_id=update.message.chat_id,
#             video=open(f"output.mp4", "rb"),
#             supports_streaming=True,
#         )
#         if os.path.exists(f"output.mp4"):
#             os.remove(f"output.mp4")
#     except instaloader.ProfileNotExistsException:
#         update.message.reply_text(f"{link_video} is not Found")
#     except instaloader.ConnectionException:
#         update.message.reply_text("IP is Blocked Please Try After Some Time")


if __name__ == "__main__":
    bot.infinity_polling()
