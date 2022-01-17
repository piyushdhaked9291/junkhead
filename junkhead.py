from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def hello(update, context):
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


def myfile(update,context):
    with open("BIO.txt", 'r') as f:
        text = f.read()
    update.message.reply_text(text)

def downloadcse423(update,context):
   context.bot.sendDocument(update.effective_chat.id, document=open("CSE423 cloud.pdf", 'rb'))

def downloadcse375(update,context):
    context.bot.sendDocument(update.effective_chat.id, document=open("CSE375 (testing).pdf", 'rb'))


def main():
    updater = Updater('5033524993:AAG0QxeoeV-im4Wbb7HOHZZvLYhLaS_YZfs')

    updater.dispatcher.add_handler(CommandHandler('hello', hello))
    updater.dispatcher.add_handler(CommandHandler('dev', myfile))
    updater.dispatcher.add_handler(CommandHandler('download', downloadcse423))
    updater.dispatcher.add_handler(CommandHandler('download', downloadcse375))


    updater.start_polling()
    updater.idle()
    

if __name__ == "__main__":
    main()





