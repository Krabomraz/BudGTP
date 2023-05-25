import telebot

from telebot import types
import os
from dotenv import load_dotenv

import telegram
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from method_pipelines.add_transaction import AddTransactionPipeline
from method_pipelines.show_transactions import ShowTransactionsPipeline

load_dotenv()

# App and DB init
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

db = SQLAlchemy(app)
bot = telebot.TeleBot(token='5815582966:AAFB6exWJ0ioABiGZfOx8vb8ZAq28BAE0yo')

menu_extra_commands = {
    '/add_transaction': 'Add transaction to database',
    '/show_transactions': 'Show transaction list',
}
bot.set_my_commands([
        types.BotCommand(k, v) for k, v in menu_extra_commands.items()
    ])

@bot.message_handler(commands=['add_transaction'])
def add_transaction(message: types.Message):
    pipeline = AddTransactionPipeline(bot)
    pipeline(message)
migrate = Migrate(app, db)

from models import *

# TG Bot init
bot = telegram.Bot(token=os.getenv('TG_BOT_API_TOKEN'))


@bot.message_handler(commands=['show_transactions'])
def show_transactions(message: types.Message):
    pipeline = ShowTransactionsPipeline(bot)
    pipeline(message)


# @app.route('/webhook', methods=['POST'])
# def webhook():
#     # update = telegram.Update.de_json(request.get_json(force=True), bot)
#     # process_update(update)
#     return 'OK'


if __name__ == '__main__':
<<<<<<< HEAD
    bot.polling(none_stop=True, interval=0)
    # app.run()
=======
    with app.app_context():
        db.create_all()
    app.run()
>>>>>>> a3a13d200b9ce34ee62d93e340c4bf122bdd719d
