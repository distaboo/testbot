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
itembtnPhoto = types.KeyboardButton('Фото наших елок')
itembtnCall = types.KeyboardButton('Связаться с нами')
itembtnAdress = types.KeyboardButton('Адрес точки продаж')
main_markup.row(itembtnAdress)
main_markup.row(itembtnPhoto)
main_markup.row(itembtnCall)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "hello", reply_markup=main_markup)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if (message.text == 'Связаться с нами') : bot.send_message(message.chat.id, "hello", reply_markup=markup)
    elif (message.text == 'Вернуться в меню'): bot.send_message(message.chat.id, "hello", reply_markup=main_markup)
    elif (message.text == 'Адрес точки продаж'):
        bot.send_message(message.chat.id,
                         "Мы находимся на парковке Сибирского Молла. Вы легко найдете нас по запаху настоящей ели.",
                         reply_markup=main_markup)
        bot.send_location(message.chat.id, 55.038377, 82.962474)
    elif (message.text == 'Фото наших елок'):
        bot.send_message(message.chat.id,
                         "Вот таких красавиц мы хотим вам предложить.",
                         reply_markup=main_markup)
        bot.send_photo(message.chat.id, open('1.png', 'rb'))
        bot.send_photo(message.chat.id, open('2.png', 'rb'))
    elif (message.text == 'Позвонить'):
        bot.send_contact(message.chat.id,+79231513104,'Алексей')


bot.polling()