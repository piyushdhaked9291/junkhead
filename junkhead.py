import telebot
API_KEY = '5033524993:AAFvJCXlR-Aq3cGneJ09IS3oxzmwHP-CrUg'
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands = ['Help','help'])
def help(message):
  bot.reply_to(message, "Created by PIYUSH DHAKED - LPU Student")


@bot.message_handler(commands=['Hello','hello'])
def hello(message):
  bot.send_message(message.chat.id, "Hey! how's it going..?")


bot.polling()