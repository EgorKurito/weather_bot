'''______________________Импорт нужных билиотек__________________________'''

import logging

import pyowm
from pyowm import OWM

import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


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

'''______________________Основные функции__________________________'''

def start(bot, update):
    """ Welcome a user to the chat """
    message = update.message
    chat_id = message.chat_id

    bot.sendMessage(chat_id = chat_id, text = "Dfsf", reply_to_message_id = message.message_id)
    if len(cities) == 0:
        bot.sendMessage(chat_id = chat_id, text = text)
    elif len(cities) == 1:
        first_keyboard = [[ str(cities[0]) ]]
        first_markup = telegram.ReplyKeyboardMarkup(first_keyboard)
        bot.sendMessage(chat_id = chat_id, text = text, reply_markup = first_markup)
    elif len(cities) == 2:
        second_keyboard = [[ str(cities[0]), str(cities[1]) ]]
        second_markup = telegram.ReplyKeyboardMarkup(second_keyboard)
        bot.sendMessage(chat_id = chat_id, text = text, reply_markup = second_markup)
    else:
        return None

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




for city in town_keyboard:
    for town in city:
        if text == town:
            bot.sendMessage(chat_id = chat_id, text = "Погода")
        else:
            town_keyboard.append([text])
            bot.sendMessage(chat_id = chat_id, text = "Город сохранен", reply_markup = town_markup)
