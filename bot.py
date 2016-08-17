# Импорт нужных библиотек
from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler
from telegram.ext import MessageHandler, Filters
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler
import logging

updater = Updater(token = '236649244:AAEhWLRS1dSQQLnk2im6Q9v-dkvxhGD0FN4')
dispatcher = updater.dispatcher


logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                  level = logging.INFO)


# Функция отвечающая за команду '/start'
def start(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text = "I'm a bot, please talk to me!")
# Вызов функции 'start'
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Функция отвечающая за повторение текста вводящих пользователем
def echo(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text = update.message.text)
# Вызов функции 'echo'
echo_handler = MessageHandler([Filters.text], echo)
dispatcher.add_handler(echo_handler)

# Функция отвечающая за поднятие регистра введенного текста
def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.sendMessage(chat_id = update.message.chat_id, text = text_caps)
# Вызов функции 'caps'
caps_handler = CommandHandler('caps', caps, pass_args = True)
dispatcher.add_handler(caps_handler)

# Фунция реализация 'Inline mode' поднятие регистра
def inline_caps(bot, update):
    query = update.inline_query.query
    #if not query:
    #    return
    result = list()
    result.append(
        InlineQueryResultArticle(
            id = query.upper(),
            title = 'caps',
            input_message_content = InputTextMessageContent(query.upper())
        )
    )
    bot.answerInlineQuery(update.inline_query.id, results = result)
# Вызов фунции 'caps' с inline mode
inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)

# Функция отвечающая за вывод ошибки при вводе несуществующей комманды
def unknown(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text = "Sorry, I didn't understand that command!")
# Вызов функции 'unknown'
unknown_handler = MessageHandler([Filters.command], unknown)
dispatcher.add_handler(unknown_handler)

# Старт бота
updater.start_polling()

updater.idle()
