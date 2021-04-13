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

@dp.message_handler(commands = ['start'])
async def echoStart(message: Message):
    await message.answer(text = '👋Hello')

@dp.message_handler(commands = ['addWord'])
async def echoHelp(message: Message):
    await message.answer(text = callCommand('/addWord', message.text.replace('/addWord ', '')), message.from_user.id)

@dp.message_handler(commands = ['removeWord'])
async def echoHelp(message: Message):
    await message.answer(text = callCommand('/removeWord', message.text.replace('/removeWord ', '')), message.from_user.id)

@dp.message_handler(commands = ['checkWord'])
async def echoHelp(message: Message):
    await message.answer(text = callCommand('/checkWord', message.text.replace('/checkWord ', '')), message.from_user.id)

@dp.message_handler(content_types = ['voice'])
async def echoAudioMessage(message: Message):
    await users.unBanUser(message)

@dp.message_handler(content_types = ContentType.TEXT)
async def echoMessage(message: Message):
    users.newUser(message)
    await processing.checkMessage(message)
