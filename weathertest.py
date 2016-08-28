'''______________________Импорт нужных билиотек__________________________'''

import logging

import pyowm
from pyowm import OWM

import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import sqlite3
from SQLighter import SQLighter

'''______________________Настройка авторизации__________________________'''

root = logging.getLogger()
root.setLevel(logging.INFO)

logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                  level = logging.INFO)

logger = logging.getLogger(__name__)

'''_____________________Глобальные переменные___________________________'''

# Токен бота
updater = Updater(token = '236649244:AAEhWLRS1dSQQLnk2im6Q9v-dkvxhGD0FN4')
# Токен API погоды
owm = OWM('a66952168b007928153234c13aa8970d', language = 'ru')
cities = []

'''______________________Клавиатуры__________________________'''



'''______________________Основные функции__________________________'''

def start(bot, update):
    """ Welcome a user to the chat """
    message = update.message
    chat_id = message.chat_id

    first_keyboard = [[ "/setting" ]]
    first_markup = telegram.ReplyKeyboardMarkup(first_keyboard)

    second_keyboard = [[ "/setting",
                         str(cities[0]) ]]
    second_markup = telegram.ReplyKeyboardMarkup(second_keyboard)

    if len(cities) == 0:
        bot.sendMessage(chat_id = chat_id, text = 'Введи свой город в формате "Moscow,RU", или выберите одну из комманд', reply_markup = first_markup)
    elif len(cities) == 1:
        bot.sendMessage(chat_id = chat_id, text = 'Введи свой город в формате "Moscow,RU", или выберите одну из комманд', reply_markup = second_markup)
    else:
        bot.sendMessage(chat_id = chat_id,text = "Введите хотябы один город")

def echo(bot, update):
    message = update.message
    chat_id = message.chat_id

    cities.append(message.text)

def get_weather(bot, update):
    message = update.message
    chat_id = message.chat_id

    obs = owm.weather_at_place(cities[0])
    w = obs.get_weather()

    temp = str(round(w.get_temperature(unit='celsius').get('temp')))
    status = str(w.get_detailed_status())

    bot.sendMessage(chat_id=chat_id, text = "Температура: " + temp +", состояние погоды: " + status)

def main():
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(MessageHandler([Filters.text], echo))

    dp.add_handler(CommandHandler("get_weather", get_weather))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
