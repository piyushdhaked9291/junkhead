from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler


def hello(update, context):
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


def myfile(update, context):
    with open("BIO.txt", 'r') as f:
        text = f.read()
    update.message.reply_text(text)


def downloadcse423(update, context):
    context.bot.sendDocument(update.effective_chat.id,
                             document=open("CSE423 cloud.pdf", 'rb'))


def downloadcse375(update, context):
    context.bot.sendDocument(update.effective_chat.id,
                             document=open("CSE375 (testing).pdf", 'rb'))


def downloadcse376(update, context):
    context.bot.sendDocument(update.effective_chat.id,
                             document=open("CSE376 Atomated.pdf", 'rb'))


def downloadint332(update, context):
    context.bot.sendDocument(update.effective_chat.id,
                             document=open("CSE375 (testing).pdf", 'rb'))


def my_button_function(update, context):
    buttons = [
        [
            InlineKeyboardButton(
                "download1",
                callback_data="down#1"
            )
        ],
        [
            InlineKeyboardButton(
                "download2",
                callback_data="down#2"
            )
        ],
        [
            InlineKeyboardButton(
                "download3",
                callback_data="down#3"
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(buttons)

    update.message.reply_text(
        text="`Hey! select any Button to download`",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )


def button_callback_function(update, context):
    query = update.callback_query
    data = query.data
    number = data.split("#")[-1]
    chat_id = query.message.chat_id
    if number == "1":
        downloadcse375(query, context)
    elif number == "2":
        downloadcse376(query, context)
    elif number == "3":
        downloadcse423(query, context)
    else:
        context.bot.send_message(
            chat_id=chat_id,
            text="❗kuch nahi mila",
        )
    context.bot.send_message(
        chat_id=chat_id,
        text=f"User selected download button {number}"
    )


def main():
    updater = Updater('5033524993:AAG0QxeoeV-im4Wbb7HOHZZvLYhLaS_YZfs')

    updater.dispatcher.add_handler(CommandHandler('hello', hello))
    updater.dispatcher.add_handler(CommandHandler('dev', myfile))

    updater.dispatcher.add_handler(CommandHandler(
        "download", my_button_function, run_async=True))
    updater.dispatcher.add_handler(CallbackQueryHandler(
        callback=button_callback_function,
        pattern="^down#"
    ))

    # updater.dispatcher.add_handler(
    #     CommandHandler('downloadcse423', downloadcse423))
    # updater.dispatcher.add_handler(
    #     CommandHandler('downloadcse375', downloadcse375))
    # updater.dispatcher.add_handler(
    #     CommandHandler('downloadint332', downloadint332))
    # updater.dispatcher.add_handler(
    #     CommandHandler('downloadcse376', downloadcse376))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
