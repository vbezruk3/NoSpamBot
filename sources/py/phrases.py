import re

from config import *

from itertools import groupby

import files

import asyncio

Words = files.loadFile(WordsPath)

def isProfane(text):

    wordsFind = re.findall(r"\S+", text)

    print(text)

    for word in Words:
        for wordFind in wordsFind:
            withDublChecker = [el for el, _ in groupby(wordFind.lower())]
            withDublWord = ''.join(withDublChecker)
            if word['text'].upper() == wordFind.upper():
                return True
            elif withDublWord.upper() == word['text'].upper():
                return True
    return False



