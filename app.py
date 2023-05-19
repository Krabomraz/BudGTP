import telegram
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/budgpt'
db = SQLAlchemy(app)
bot = telegram.Bot(token='6040180287:AAHIxIYOz3HseQ5Ushel49lfuyuLm8EuJek')


@app.route('/webhook', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    process_update(update)
    return 'OK'


def process_update(update):
    # Implement your bot logic here
    message = update.message
    chat_id = message.chat_id
    text = message.text

    # Example response
    response_text = f"You said: {text}"
    bot.send_message(chat_id=chat_id, text=response_text)


if __name__ == '__main__':
    app.run()
