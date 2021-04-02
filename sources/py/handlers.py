import sys

import processing

import users

import subprocess

import phrases

import asyncio

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

@dp.message_handler(content_types=['voice'])
async def echoAudioMessage(message: Message):
    await users.unBanUser(message)

@dp.message_handler(content_types = ContentType.TEXT)
async def echoMessage(message: Message):
    users.newUser(message)
    await processing.checkMessage(message)
