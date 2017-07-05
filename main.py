# Importing libraries and packages
import weather, config
import telegram, logging, pyowm

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from pyowm import OWM

# Main variable
updater = Updater(token = config.BOT_TOKEN)

owm = OWM(config.WEATHER_TOKEN, language = 'ru')

# Bot authentication
root = logging.getLogger()
root.setLevel(logging.INFO)

logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                  level = logging.INFO)

logger = logging.getLogger(__name__)

# Main function
def main():
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", weather.start))
    dp.add_handler(MessageHandler([Filters.text], weather.city))
    dp.add_handler(CommandHandler('delete', weather.delete, pass_args=True))
    dp.add_handler(MessageHandler([Filters.command], weather.unknown))

    updater.start_webhook(listen='0.0.0.0', port=config.PORT, url_path=config.BOT_TOKEN)
    updater.bot.setWebhook(config.URL + '/' + config.BOT_TOKEN)
    updater.idle()


if __name__ == '__main__':
    main()
