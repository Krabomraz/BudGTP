import telebot

from telebot import types
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from method_pipelines.add_transaction import AddTransactionPipeline
from method_pipelines.show_transactions import ShowTransactionsPipeline

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/budgpt'
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
    bot.polling(none_stop=True, interval=0)
    # app.run()
