import dataAcess.askDA as askDB


askList = {}


def init():
    global askList
    list = askDB.getAsk()
    for item in list:
        askList[item["id"]] = int(item["text"])


def getAskOption(userID):
    list = askDB.getAskOption(userID)
    response = [askList[1], askList[2], askList[3], askList[4]]
    for item in list:
        response.append(askList[item["ask_id"]])

    return response


def addAskOption(userID, askID):
    if askDB.verifyAskOption(userID, askID):
        return 5
    askDB.addAskOption(userID, askID)
    return 4
