import logging
from aiogram import Bot, Dispatcher, executor, types

from mods.core_plug import start_msg, help_msg

class bot:
    def __init__(self, api_token: str):
        logging.basicConfig(level=logging.INFO)
        self.b: Bot = Bot(api_token)

        self.dp: Dispatcher = Dispatcher(self.b)
        self.pre_init()
        executor.start_polling(self.dp, skip_updates=True)

    def pre_init(self):
        self.dp.register_message_handler(start_msg, commands=["start"])
        self.dp.register_message_handler(help_msg, commands=["help"])


    def load_modules(self):
        pass