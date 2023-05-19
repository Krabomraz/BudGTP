import os
import telegram
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://#{os.getenv('DB_USER')}:#{os.getenv('DB_PASSWORD')}@#{os.getenv('DB_HOST')}/#{os.getenv('DB_NAME')}"
db = SQLAlchemy(app)
bot = telegram.Bot(token=os.getenv('TG_BOT_API_TOKEN'))


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
