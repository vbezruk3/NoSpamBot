import json, codecs, os, files, tree    #Работаем с json

import asyncio

from config import *

accesses = {}

def load():
    global accesses

    accesses = files.loadFile(AccessesPath)
   
def save():
    files.saveFile(accesses, AccessesPath)

def check(access):
    if accesses.get(access) == None:
        return False
    return True

def add(access, command):
    if check(access) and not accesses[access].count(command):
        accesses[access].append(command)
        return True
    return False

def remove(access, command):
    if check(access) and accesses[access].count(command) > 0:
        accesses[access].remove(command)
        return True
    else:
        return False

def getCommands(access):

    if check(access):
        result = f'In access level {access} available commands:'

        for command in accesses[access]:
            result += f'\n\t{command}'

    else:
        result = f'There is no {access} level of access\n'

    return result

def checkCommand(access, command):
    if check(access) and accesses[access].count(command) > 0:
        return True
    else:
        return False



load()

