'''______________________Импорт нужных билиотек__________________________'''

import logging
import os

import pyowm
from pyowm import OWM

import telegram
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

'''______________________Настройка авторизации__________________________'''

root = logging.getLogger()
root.setLevel(logging.INFO)

logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                  level = logging.INFO)

logger = logging.getLogger(__name__)

'''_____________________Глобальные переменные___________________________'''

# Токен бота
TOKEN = '236649244:AAEhWLRS1dSQQLnk2im6Q9v-dkvxhGD0FN4'
updater = Updater(token = '236649244:AAEhWLRS1dSQQLnk2im6Q9v-dkvxhGD0FN4')
# Токен API погоды
owm = OWM('a66952168b007928153234c13aa8970d', language = 'ru')
hide_markup = telegram.ReplyKeyboardHide()

towns = [] # list of city
town_keyboard = [towns,["Remove city"]]
town_markup = telegram.ReplyKeyboardMarkup(town_keyboard, resize_keyboard = True)

remove_towns = []
remove_keyboard = [remove_towns]
remove_markup = telegram.ReplyKeyboardMarkup(remove_keyboard)

'''______________________Основные функции__________________________'''

def start(bot, update):
    message = update.message
    chat_id = message.chat_id

    bot.sendMessage(chat_id = chat_id, text = "Введите город для сохранения", reply_markup = town_markup)

def city(bot, update):
    message = update.message
    chat_id = message.chat_id
    text = message.text

    if text == "Remove city":
        bot.sendMessage(chat_id = chat_id, text = "Выберите город который хотите удалить", reply_markup = remove_markup)
    else:
        if len(towns) == 0:
            towns.append(text)
            remove_towns.append("/delete " + text)
            bot.sendMessage(chat_id = chat_id, text = "Сохранили", reply_markup = town_markup)
        elif len(towns) == 1:
            if text == towns[0] and "/delete " + text == remove_towns[0]:
                get_weather(bot, update, text)
            else:
                towns.append(text)
                remove_towns.append("/delete " + text)
                bot.sendMessage(chat_id = chat_id, text = "Сохранили", reply_markup = town_markup)
        elif len(towns) == 2:
            if (text == towns[0] or text == towns[1]) and ("/delete " + text == remove_towns[0] or "/delete " + text == remove_towns[1]):
                get_weather(bot, update, text)
            else:
                towns.append(text)
                remove_towns.append("/delete " + text)
                bot.sendMessage(chat_id = chat_id, text = "Сохранили", reply_markup = town_markup)
        else:
            get_weather(bot, update, text)

def get_weather(bot, update, text):
    message = update.message
    chat_id = message.chat_id

    obs = owm.weather_at_place(text)
    w = obs.get_weather()

    temp = str(round(w.get_temperature(unit='celsius').get('temp')))
    status = str(w.get_detailed_status())

    bot.sendMessage(chat_id=chat_id, text = "Температура: " + temp +", состояние погоды: " + status)

def delete(bot, update, args):
    message = update.message
    chat_id = message.chat_id

    try:
        towns.remove(args[0])
        remove_towns.remove("/delete " + args[0])
        bot.sendMessage(chat_id = chat_id, text = "Город удален", reply_markup = town_markup)
    except ValueError:
        bot.sendMessage(chat_id = chat_id, text = "Этого города не существует", reply_markup = town_markup)

# Функция отвечающая за вывод ошибки при вводе несуществующей комманды
def unknown(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text = "Я не знаю эту команду(")

def main():
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler([Filters.text], city))
    dp.add_handler(CommandHandler('delete',delete, pass_args=True))
    dp.add_handler(MessageHandler([Filters.command], unknown))
    updater.start_polling()

    PORT = int(os.environ.get('PORT', '5000'))
    updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
    updater.bot.setWebhook("https://weatheregorbot.herokuapp.com/" + TOKEN)

    updater.idle()


if __name__ == '__main__':
    main()
