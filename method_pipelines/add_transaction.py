from typing import Any
import telebot

from telebot import types


class AddTransactionPipeline():
    def __init__(self, bot: telebot.TeleBot) -> None:
        self._bot = bot

    def __call__(self, message: types.Message) -> None:
        self._bot.send_message(message.chat.id, "Через ';' перечисли: купля или продажа;категория;номинал;валюта")
        self._bot.register_next_step_handler(message, self._collect_transaction)

    def _collect_transaction(self, message: types.Message) -> None:
        # Логика по отправке на backend
        pass

        self._bot.send_message(message.chat.id, "Запись успешно добавлена")
