import accesses, users, phrases

def callCommand(command, arg, t_id):
    if users.checkCommand(t_id, command) == False:
        return 'You do not have access to this command'
    else:
        if command == '/addWord':
            return phrases.addWord(arg)
        if command == '/removeWord':
            return phrases.removeWord(arg)
        if command == '/checkWord':
            return phrases.checkWord(arg)
        if command == '/checkProfane':
            return phrases.isProfane(phrases.reformatWord(arg, 'ru')) or phrases.isProfane(phrases.reformatWord(arg, 'en'))