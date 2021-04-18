import re

from config import *

from itertools import groupby

import files

import asyncio

Letters = files.loadFile(LettersPath)
Words = files.loadFile(WordsPath)

def reformatLetter(let, lang):
    for key in Letters[lang].keys():
        if let in Letters[lang][key]:
            return key
    return let

def reformatWord(text, lang):
    newText = ''

    text = text.lower()

    for let in text:
        newText = newText + reformatLetter(let, lang)

    return newText

def isProfane(text):

    wordsFind = re.findall(r"\S+", text)

    for word in Words:
        for wordFind in wordsFind:
            withDublChecker = [el for el, _ in groupby(wordFind.lower())]
            withDublWord = ''.join(withDublChecker)
            if word['text'].upper() == wordFind.upper():
                return True
            elif withDublWord.upper() == word['text'].upper():
                return True
    return False

def createWord(text):

    word = {}

    word['number'] = int(len(Words) + 1)
    word['text'] = str(text)
    word['repeat'] = 0

    return word

def checkWord(text):

    for word in Words:
        if word['text'] == text:
            return True
    return False

def findWord(text):

    i = 0

    for word in Words:
        if word['text'] == text:
            return i
        i = i + 1

    return -1

def addWord(text):

    if checkWord(text) == False:
        Words.append(createWord(text))
        files.saveFile(Words, WordsPath)
        return f'Aded word "{text}"'
    else:
        return f'Word "{text}" already aded!'

def removeWord(text):

    if checkWord(text) == True:

        i = findWord(text)

        Words.pop(i)

        for j in range (i, len(Words)):
            Words[j]['number'] = int(Words[j]['number']) - 1

        files.saveFile(Words, WordsPath)
        return f'Word {text} removed'
    else:
        return f'There is no word {text} in the database'