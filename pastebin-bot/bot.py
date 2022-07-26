from API import API_KEY
import telegram.ext
import os, subprocess
from request import file_writer, file_remover
from insta_profile import profile_downloader, profile_delete


def start(update, context):
    update.message.reply_text("Welcome to PasteBin Bot Powered by paste.rs/web")


def help(update, context):
    update.message.reply_text("""
    
    The Following Commands can we user
    
    /start - to say welcome message
    /help - to get help
    /paste <content> - to push content to paste.rs
    /pic <insta user name> - to download a reels from instagram
    
    """)


def paste(update, context):
    data = context.args[::]
    listToStr = ' '.join(map(str, data))
    file_writer(text=listToStr)
    output = subprocess.check_output('curl --data-binary @file.txt https://paste.rs/', shell=True)
    update.message.reply_text(f"{output.decode('utf-8')}")
    file_remover()


def pic(update, context):
    username = context.args[0]
    try:
        profile_downloader(username=username)
        for root, subdirs, files in os.walk(username):
            for file in files:
                if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg'):
                    context.bot.send_photo(chat_id=update.message.chat_id,
                                           photo=open(f'{os.path.join(root, file)}', 'rb'))
        profile_delete(username=username)
    except:
        update.message.reply_text(f"{username} is not found")


updater = telegram.ext.Updater(API_KEY, use_context=True)

disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("paste", paste))
disp.add_handler(telegram.ext.CommandHandler("pic", pic))

updater.start_polling()
updater.idle()
