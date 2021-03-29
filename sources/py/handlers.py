import sys

import users

import subprocess

import phrases

from main import bot, dp

from aiogram.types import Message, User, ContentType

from collections import Counter

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

@dp.message_handler(content_types = ContentType.TEXT)
async def echoMessage(message: Message):
    text = message.text

    if users.checkUser(message.from_user.id) == False:
            user = {}

            user['id'] = message.from_user.id
            user['username'] = message.from_user.username
            user['ban'] = False

            users.addUser('user', user)

            users.save()

    if text and not text.startswith('/'):
        if phrases.search(text):
            #users.banUser(message.from_user.id)
            await message.reply(text = 'Bad')
        else:
            await message.reply(text='Ok')
