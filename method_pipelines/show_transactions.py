from typing import Any
import telebot

from telebot import types


class ShowTransactionsPipeline:
    def __init__(self, bot: telebot.TeleBot) -> None:
        self._bot = bot

    def __call__(self, message: types.Message) -> None:
        self._bot.send_message(message.chat.id, "Не реализованно")
