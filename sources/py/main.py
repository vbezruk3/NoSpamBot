import asyncio

from aiogram import Bot, Dispatcher, executor

from config import *

loop = asyncio.get_event_loop()

bot = Bot(config['SYSTEM']['BOT_TOKEN'], parse_mode = "HTML")

dp = Dispatcher(bot, loop = loop)

if __name__ == "__main__":
    from handlers import dp, init
    executor.start_polling(dp, on_startup = init)
