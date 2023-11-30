import dataAcess.deckDA as deckDB
import gameBoard
import sys
NUMBER_MAX_IN_HAND = 4


def addCard(userID, cardID):
    hand = 0
    if checkHandCapacity(userID):
        hand = 1
    if deckDB.isCardAlreadyUnlock(userID, cardID):
        return 5
    deckDB.addCardInDB(userID, cardID, hand)
    return 3


def getDeckStatut(user):
    statut = {}
    statut["deck"] = deckDB.getDeckWithCard(user["id"])
    statut["language"] = user["language"]
    statut["field"] = getFieldList()
    return statut


def switchCardInHand(cardID, userID):
    if not checkHandCapacity(userID):
        return
    deckDB.switchValueInHand(cardID, userID)
    return


def checkHandCapacity(userID):
    count = deckDB.checkHandCapacityInDB(userID)
    if count > NUMBER_MAX_IN_HAND:
        return False
    return True


def getFieldList():
    fields = gameBoard.fields.copy()
    del fields[0]
    fields = [field["name"] for field in fields]
    return fields
