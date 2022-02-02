from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler


def start(update, context):
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


def myfile(update, context):
    with open("BIO.txt", 'r') as f:
        text = f.read()
    erase = update.message.reply_text(text)
    context.job_queue.run_once(callback_delete, 60, context=erase)


def downloadcse423(update, context):
    context.bot.sendDocument(update.message.chat_id,
                             document=open("CSE423 cloud.pdf", 'rb'))
    context.bot.sendDocument(update.message.chat_id,
                             document=open("CSE423 VLAN.pdf", 'rb'))
    context.bot.sendDocument(update.message.chat_id,
                             document=open("CSE423 Cluster Computing.pdf", 'rb'))
    context.bot.sendDocument(update.message.chat_id,
                             document=open("CSE423 Cloud Types.pdf", 'rb'))


def downloadcse375(update, context):
    context.bot.sendDocument(update.message.chat_id,
                             document=open("CSE375 (testing).pdf", 'rb'))
    context.bot.sendDocument(update.message.chat_id,
                             document=open("CSE375 UNIT2.ppt", 'rb'))
    context.bot.sendDocument(update.message.chat_id,
                             document=open("CSE375 BlackBoxTesting.pdf", 'rb'))
    context.bot.sendDocument(update.message.chat_id,
                             document=open("CSE375 Testingtypes(WithQuestions).pdf", 'rb'))


def downloadcse376(update, context):
    context.bot.sendDocument(update.message.chat_id,
                             document=open("CSE376 Atomated.pdf", 'rb'))
    context.bot.sendDocument(update.message.chat_id,
                             document=open("Junit.pdf", 'rb'))


def downloadint332(update, context):
    context.bot.sendDocument(update.message.chat_id,
                             document=open("Dockerization 1.pdf", 'rb'))
    context.bot.sendDocument(update.message.chat_id,
                             document=open("Docker Architecture.pdf", 'rb'))
    context.bot.sendDocument(update.message.chat_id,
                             document=open("Docker Practical.pdf", 'rb'))
    context.bot.sendDocument(update.message.chat_id,
                             document=open("INT332 prac2.pdf", 'rb'))
    context.bot.sendDocument(update.message.chat_id,
                             document=open("INT332 Practical-Hyper-V.pdf", 'rb'))


def my_button_function(update, context):
    buttons = [
        [
            InlineKeyboardButton(
                "CSE 375",
                callback_data="down#1"
            )
        ],
        [
            InlineKeyboardButton(
                "CSE 376",
                callback_data="down#2"
            )
        ],
        [
            InlineKeyboardButton(
                "CSE 423",
                callback_data="down#3"
            )
        ],
        [
            InlineKeyboardButton(
                "INT 332",
                callback_data="down#4"
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(buttons)

    piyush = update.message.reply_text(
        text="`Hey! select any Button to download`",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )
    context.job_queue.run_once(callback_delete, 20, context=piyush)


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
    elif number == "4":
        downloadint332(query, context)
    else:
        context.bot.send_message(
            chat_id=chat_id,
            text="❗kuch nahi mila",
        )
    context.bot.send_message(
        chat_id=chat_id,
        text=f"User selected download button {number}"
    )


def callback_delete(context):
    context.job.context.delete()


def main():
    updater = Updater('5033524993:AAG0QxeoeV-im4Wbb7HOHZZvLYhLaS_YZfs')

    updater.dispatcher.add_handler(CommandHandler('start', start))
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
