import users

import asyncio

import subprocess

import phrases

import phrases

from main import bot, dp

from aiogram.types import Message, User, ContentType

async def checkMessage(message: Message):
    text = message.text

    if text and not text.startswith('/'):
        if phrases.isProfane(text):
            await users.profane(message)
        else:
            await users.notProfane(message)
        #    await message.reply(text = 'Bad')
        #else:
        #    await message.reply(text = 'Ok')