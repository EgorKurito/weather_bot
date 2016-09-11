import weather, config

import logging
import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def main():
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler([Filters.text], city))
    dp.add_handler(CommandHandler('delete',delete, pass_args=True))
    dp.add_handler(MessageHandler([Filters.command], unknown))
    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
