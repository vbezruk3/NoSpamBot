import json

import codecs

def loadFile(FilePath):
    with codecs.open(FilePath, encoding='utf-8') as file:
        data = json.loads(file.read())

    return data
