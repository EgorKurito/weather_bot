import telegram
import os
from flask import Flask, request
from werkzeug.contrib.fixers import ProxyFix

TOKEN = "308017424:AAEcnQMCPCaMP-s-YNVx298DFOPtR69DRFU"
PORT = int(os.environ.get('PORT', '5000'))

global bot
bot = telegram.Bot(token = TOKEN)
app = Flask(__name__)


@app.route('/'+TOKEN, methods=['POST'])
def webhook_handler():
    if request.method == "POST":
        # retrieve the message in JSON and then transform it to Telegram object
        update = telegram.Update.de_json(request.get_json(force=True))

        chat_id = update.message.chat.id

        # Telegram understands UTF-8, so encode text for unicode compatibility
        text = update.message.text.encode('utf-8')

        # repeat the same message back (echo)
        bot.sendMessage(chat_id=chat_id, text=text)

    return 'ok'


@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook("https://weatheregorbot.herokuapp.com/" + TOKEN)
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"


@app.route('/')
def index():
    return 'TEST'

app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == '__main__':
    set_webhook()
    app.run(0.0.0.0,
            port=PORT,
            debug=True)
