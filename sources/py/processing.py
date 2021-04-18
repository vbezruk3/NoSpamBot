import users

import asyncio

import subprocess

import phrases

import phrases

from main import bot, dp

from aiogram.types import Message, User, ContentType

async def checkMessage(message: Message):
    text = message.text

    if users.getAccess(message.from_user.id) == 'admin':
        await users.notProfane(message)
    else:
        if phrases.isProfane(phrases.reformatWord(text, 'ru')) or phrases.isProfane(phrases.reformatWord(text, 'en')):
            await users.profane(message)
        else:
            await users.notProfane(message)
