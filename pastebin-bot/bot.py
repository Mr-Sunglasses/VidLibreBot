from API import API_KEY
import telegram.ext
import os, subprocess
from request import file_writer, file_remover
from insta_profile import profile_downloader, profile_delete
from qr_generator import generate_qr, delete_qr
from quotes import preload_quotes, quotes
from random import randint
from love_quotes import happy_love_quotes, sad_love_quotes
from image_training import model, x_test, y_test, x_train, y_train, class_name
from io import BytesIO
import numpy as np
import cv2


def start(update, context):
    update.message.reply_text("Welcome to PasteBin Bot Powered by paste.rs/web")


def help(update, context):
    update.message.reply_text("""
    
    The Following Commands can we user
    
    /start - to say welcome message
    /help - to get help
    /paste <content> - to push content to paste.rs
    /pic <insta user name> - to download a profile pic of the user
    /qr <link of data> - to generate qr code
    /quote - for getting random quotes
    /love_quote_happy - for romantic quotes [happy]
    /love_quote_sad - for romantic quotes [sad]
    
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
        profile_delete(username=username)


def qr(update, context):
    link = context.args[0]
    try:
        generate_qr(link=link)
        context.bot.send_photo(chat_id=update.message.chat_id, photo=open('myqr.png', 'rb'))
        delete_qr()
    except:
        update.message.reply_text(f"QR of this {link} can't be generated")
        delete_qr()


def quote(update, context):
    preload_quotes()
    update.message.reply_text(f"{quotes[randint(0, 9)]}")


def love_quote_happy(update, context):
    update.message.reply_text(f"❤️ {happy_love_quotes[randint(0, 22)]}")


def love_quote_sad(update, context):
    update.message.reply_text(f"❤️ {sad_love_quotes[randint(0, 3)]}")


def train(update, context):
    update.message.reply_text("Training the model")
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))
    model.save('cifar_classifier.model')
    update.message.reply_text("Done You can now Send a Photo")


def handle_photo(update, context):
    file = context.bot.get_file(update.message.photo[-1].file_id)
    f = BytesIO(file.download_as_bytearray())
    file_byte = np.asarray(bytearray(f.read()), dtype=np.uint8)

    img = cv2.imdecode(file_byte, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    img = cv2.resize(img, (32, 32), interpolation=cv2.INTER_AREA)

    prediction = model.predict(np.array([img / 255]))
    update.message.reply_text(f"In this image I can see {class_name[np.argmax(prediction)]}")


updater = telegram.ext.Updater(API_KEY, use_context=True)

disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("paste", paste))
disp.add_handler(telegram.ext.CommandHandler("pic", pic))
disp.add_handler(telegram.ext.CommandHandler("qr", qr))
disp.add_handler(telegram.ext.CommandHandler("quote", quote))
disp.add_handler(telegram.ext.CommandHandler("train", train))
disp.add_handler(telegram.ext.CommandHandler("love_quote_happy", love_quote_happy))
disp.add_handler(telegram.ext.CommandHandler("love_quote_sad", love_quote_sad))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.photo, handle_photo))

updater.start_polling()
updater.idle()
