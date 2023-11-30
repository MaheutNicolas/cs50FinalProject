import language.textDataAcess as db

languageList = {}


def init():
    global languageList
    languageList = db.getText()


def get(langage, id):
    if langage in languageList.keys():
        return languageList[langage][id]
    return languageList["eng"][id]


def getLanguage():
    return sorted(languageList.keys())
