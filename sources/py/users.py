import json, codecs, accesses, os, files, tree   #Работаем с json

from config import *

users = {}

def load():
    global users

    users = files.loadFile(UsersPath)

def save():

    files.saveFile(users, UsersPath)
        
def checkUser(access, t_id):
    if users.get(access) == None:
        return False
    
    for user in users[access]:
        if user['id'] == t_id:
            return True
    return False
    
def addUser(access, user):
    users[access].append(user)

def searchUser(access, t_id):
    i = 0
    for user in users[access]:
        if user['id'] == t_id:
            return i 
    i = i + 1

def checkUser(t_id):
    access = getAccess(t_id)
    
    if access == None:
        return False
    else:
        return True
    
def set(access, t_id, setting, value):
    if checkUser(t_id):
        users[access][searchUser(access, t_id)][setting] = value

def get(access, t_id, setting):
    if checkUser(t_id):
        return users[access][searchUser(access, t_id)][setting]

def getAccess(t_id):
    for access in users.keys():
        for user in users[access]:
            if user['id'] == t_id:
                return access
    return None
    
def checkCommand(t_id, command):
    return accesses.checkCommand(getAccess(t_id), command)
                
load()
