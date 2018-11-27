from telebot import types
import requests
import telebot
from telebot.types import Message

TOKEN = "751120059:AAGGNfinmmdqDNYLyL2hP-FeeiMnCF3vp3E"
bot = telebot.TeleBot(TOKEN)
# or add KeyboardButton one row at a time:
markup = types.ReplyKeyboardMarkup()
itembtna = types.KeyboardButton('Позвонить')
itembtnv = types.KeyboardButton('Написать')
itembtnc = types.KeyboardButton('Оставить номер')
itembtnd = types.KeyboardButton('Вернуться в меню')

markup.row(itembtna, itembtnv)
markup.row(itembtnc, itembtnd)

main_markup = types.ReplyKeyboardMarkup()
itembtnPhoto = types.KeyboardButton('Позвонить')
itembtnCall = types.KeyboardButton('Написать')
itembtnAdress = types.KeyboardButton('Оставить номер')
main_markup.add(itembtnAdress,itembtnPhoto,itembtnCall)



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "hello", reply_markup=main_markup)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, "hello", reply_markup=markup)

bot.polling()