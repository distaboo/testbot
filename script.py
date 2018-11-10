from telebot import types
import requests
import telebot
from telebot.types import Message

TOKEN = "751120059:AAGGNfinmmdqDNYLyL2hP-FeeiMnCF3vp3E"
markup_menu = types.ReplyKeyboardMarkup(resize_keyboard = True,row_width = 1)
btn_adress = types.KeyboardButton('Список магазинов',request_location = True)
btn_payment = types.KeyboardButton('Способы оплаты')
btn_delivery = types.KeyboardButton('Способы доставки')
markup_menu.add(btn_adress,btn_payment,btn_delivery)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func = lambda message:True,commands=['start', 'help'])
def command_handler(message: Message):
    bot.reply_to(message, 'Hello', reply_markup=markup_menu)

@bot.edited_message_handler(func = lambda message:True,content_types=['text'])
@bot.message_handler(func = lambda message:True,content_types=['text'])
def echo_digits(message: Message):
        if message.text == 'Способы доставки':
            bot.reply_to(message, 'Доставка курьером, самовывоз',reply_markup = markup_menu)
        elif message.text == 'Способы оплаты':
            bot.reply_to(message, 'Nal, beznal', reply_markup=markup_menu)
        else:
            bot.reply_to(message, 'Alex is good kid',reply_markup = markup_menu)
        return
@bot.message_handler(func = lambda message:True,content_types=['location'])
def location(message: Message):
    lon = message.location.longitude
    lat = message.location.latititude
    print('Широта: {} Долгота: {}'.format(lon,lat))
bot.polling(timeout=60)