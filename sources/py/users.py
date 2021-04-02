import json, codecs, accesses, os, files, tree   #Работаем с json

from aiogram.types import Message, User, ContentType

from config import *

import asyncio

import subprocess

import phrases

from main import bot, dp

users = {}

def load():
    global users

    users = files.loadFile(UsersPath)

def save():

    files.saveFile(users, UsersPath)

def addUser(access, user):
    users[access].append(user)

def searchUser(access, t_id):
    i = 0
    for user in users[access]:
        if str(user['id']) == str(t_id):
            return i
        i = i + 1
    return -1

def checkUserAccess(access, t_id):
    if users.get(access) == None:
        return False

    if searchUser(access, t_id) == -1:
        return False
    else:
        return True

def checkUser(t_id):
    for access in users.keys():
        if checkUserAccess(access, t_id) == True:
            return True
    return False

def set(access, t_id, setting, value):
    if checkUser(t_id):
        users[access][searchUser(access, t_id)][setting] = value

def get(access, t_id, setting):
    if checkUser(t_id):
        return users[access][searchUser(access, t_id)][setting]

def getAccess(t_id):
    for access in users.keys():
        for user in users[access]:
            if str(user['id']) == str(t_id):
                return access
    return None

def checkCommand(t_id, command):
    return accesses.checkCommand(getAccess(t_id), command)

def checkBan(t_id):
    return get(getAccess(t_id), t_id, 'ban')

def createUser(message: Message):
    user = {}

    user['id'] = message.from_user.id
    user['username'] = message.from_user.username
    user['ban'] = 0
    user['ban_count'] = 0

    return user

def newUser(message: Message):
    if checkUser(message.from_user.id) == False:
        addUser('user', createUser(message))

        save()

def banUser(t_id, ban):
    set(getAccess(t_id), t_id, 'ban', ban)

    save()

def banUserAlways(t_id):
    set(getAccess(t_id), t_id, 'ban', 2)

def countBan(t_id):
    current = get(getAccess(t_id), t_id, 'ban_count')
    set(getAccess(t_id), t_id, 'ban_count', current + 1)

    save()

def getBanCount(t_id):
    return get(getAccess(t_id), t_id, 'ban_count')

async def notProfane(message: Message):
    if checkBan(message.from_user.id) == 1:
        await message.reply(text='Ти тимчасово забанений\n' +
                                 'Відправ віршик, щоб повернути довіру до тебе\n')
        await bot.delete_message(message.chat.id, message.message_id)

async def profane(message: Message):

    if getBanCount(message.from_user.id) < config['SYSTEM']['MAX_BAN_COUNT']:
        countBan(message.from_user.id)

    if getBanCount(message.from_user.id) == config['SYSTEM']['MAX_BAN_COUNT']:
        banUserAlways(message.from_user.id)

    if checkBan(message.from_user.id) != 2:
        if checkBan(message.from_user.id) == 0:

            remain = config['SYSTEM']['MAX_BAN_COUNT'] - getBanCount(message.from_user.id)

            await message.reply(text = 'Ти тимчасово забанений\n' +
                                       f'Ще {remain} таких викрутасів і ти будеш назавжди забанений\n' +
                                       'Відправ віршик, щоб повернути довіру до тебе\n')
        banUser(message.from_user.id, 1)

    await bot.delete_message(message.chat.id, message.message_id)

async def unBanUser(message: Message):
    if checkBan(message.from_user.id) == 1:
        banUser(message.from_user.id, 0)
        await message.reply(text = 'Ти розбанений!')

load()
