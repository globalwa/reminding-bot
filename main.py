from config_reader import config

import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

logging.basicConfig(level=logging.INFO)

dp = Dispatcher()

@dp.message(Command(commands=["start"]))
async def cmd_start(message: Message) -> None:
    await message.answer(f"Hello, {message.from_user.full_name}")

def main() -> None:
    bot = Bot(token=config.bot_token.get_secret_value())
    dp.run_polling(bot)

if __name__ == "__main__":
    main()