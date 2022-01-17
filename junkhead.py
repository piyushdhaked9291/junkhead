from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def hello(update, context):
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


def myfile(update,context):
    with open("BIO.txt", 'r') as f:
        text = f.read()
    update.message.reply_text(text)

def download(update,context):
    update.message.sendDocument(update.effective_chat.id, document=open("CSE423-cloud.pdf", 'rb'))

    

updater = Updater('5033524993:AAG0QxeoeV-im4Wbb7HOHZZvLYhLaS_YZfs')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('dev', myfile))
updater.dispatcher.add_handler(CommandHandler('download', download))


updater.start_polling()
updater.idle()