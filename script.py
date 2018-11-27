from telebot import types
import requests
import telebot
from telebot.types import Message

TOKEN = "751120059:AAGGNfinmmdqDNYLyL2hP-FeeiMnCF3vp3E"
bot = telebot.TeleBot(TOKEN)
# or add KeyboardButton one row at a time:
markup = types.ReplyKeyboardMarkup()
itembtna = types.KeyboardButton('a')
itembtnv = types.KeyboardButton('v')
itembtnc = types.KeyboardButton('c')
itembtnd = types.KeyboardButton('d')
itembtne = types.KeyboardButton('e')
markup.row(itembtna, itembtnv)
markup.row(itembtnc, itembtnd, itembtne)


@bot.message_handler(func = lambda message:True,commands=['start', 'help'])
def command_handler(message: Message):
    bot.reply_to(message, 'Hello', reply_markup=markup_menu)

@bot.edited_message_handler(func = lambda message:True,content_types=['text'])
@bot.message_handler(func = lambda message:True,content_types=['text'])
def echo_digits(message: Message):
        bot.send_message(message.chat_id, "Choose one letter:", reply_markup=markup)

        return

bot.polling(timeout=60)