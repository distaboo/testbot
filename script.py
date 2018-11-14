from telebot import types
import requests
import telebot
from telebot.types import Message

TOKEN = "751120059:AAGGNfinmmdqDNYLyL2hP-FeeiMnCF3vp3E"
markup_menu = types.ReplyKeyboardMarkup(resize_keyboard = True,row_width = 1)
btn_adress = types.KeyboardButton('Адреса точек продаж')
btn_payment = types.KeyboardButton('Наши елки')
btn_delivery = types.KeyboardButton('Связаться с нами')
markup_menu.add(btn_adress,btn_payment,btn_delivery)

contact_inline = types.InlineKeyboardMarkup()
btn_call = types.InlineKeyboardButton('Позвонить', callback_data='cash')
btn_message = types.InlineKeyboardButton('Написать', callback_data='card')
btn_number = types.InlineKeyboardButton('Оставить номер', callback_data='card')
contact_inline.add(btn_call,btn_message,btn_number)




bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func = lambda message:True,commands=['start', 'help'])
def command_handler(message: Message):
    bot.reply_to(message, 'Hello', reply_markup=markup_menu)

@bot.edited_message_handler(func = lambda message:True,content_types=['text'])
@bot.message_handler(func = lambda message:True,content_types=['text'])
def echo_digits(message: Message):
        if message.text == 'Способы доставки':
            bot.reply_to(message, 'Доставка курьером, самовывоз',reply_markup = markup_menu)
        elif message.text == 'Связаться с нами':
            bot.reply_to(message, 'Позвоните нам или напишите в телеграм. '
                                  'Также вы можете оставить нам свой номер и наш менеджер сам с вами свяжется',
                         reply_markup=contact_inline)
        return
@bot.message_handler(func = lambda message:True,content_types=['location'])
def location(message: Message):
    lon = message.location.longitude
    lat = message.location.latititude
    print('Широта: {} Долгота: {}'.format(lon,lat))

#@bot.message_handler(func = lambda message:True,content_types=['contact'])
#def location(message: Message):
#    bot.send_message(message.chat.id, text=message.contact)

@bot.callback_query_handler(func = lambda call:True)
def call_back_pay(call):
    if call.data == 'cash':
        bot.send_message(call.message.chat.id,text='Вы оплатили наличными')
    if call.data == 'card':
        bot.send_message(call.message.chat.id,text='Вы оплатили наличными')



bot.polling(timeout=60)