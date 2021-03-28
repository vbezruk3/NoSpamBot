import re

from config import *

import files

Words = files.loadFile(WordsPath)

def search(text):

    wordsFind = re.findall(r"\S+", text)

    print(wordsFind)

    for word in Words:

        for wordFind in wordsFind:
            if word['text'].upper() == wordFind.upper():
                return True
    return False



