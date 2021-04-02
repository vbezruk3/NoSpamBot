import re

from config import *

import files

import asyncio

Words = files.loadFile(WordsPath)

def isProfane(text):

    wordsFind = re.findall(r"\S+", text)

    print(text)

    for word in Words:
        for wordFind in wordsFind:
            if word['text'].upper() == wordFind.upper():
                return True
    return False



