import sys

import subprocess

from main import bot, dp

from aiogram.types import Message, User

from collections import Counter

sys.path.append('../../config/')

from config import *

async def init(dp):
    await bot.send_message(chat_id = config['SYSTEM']['ADMIN_ID'], text = 'Bot started!')

@dp.message_handler(commands=['start'])
async def echoStart(message: Message):
    await message.answer(text = '👋Hello')
'''
@dp.message_handler(commands=['help'])
async def echoHelp(message: Message):
'''
