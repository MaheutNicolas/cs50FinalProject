import dataAcess.userDA as userDB
from dataAcess.deckDA import getDeck
import gameBoard
import service.effectService as effect
import language.text as text
import sys

# ---------- GET -------------


def getStatut(user):
    statut = {}
    statut["field"] = user["field"]
    statut["language"] = user["language"]

    if statut["field"] == "lobby" or statut["field"] == "victory":
        statut["languageList"] = text.getLanguage()
        return statut

    statut["pos"] = user["pos"]
    statut["cards"] = getCardsList(user)
    statut["deck"] = getDeckList(user["id"])
    return statut


def getCardsList(user):
    fieldID = gameBoard.getFieldID(user["field"])
    if fieldID == "error":
        return "error"
    maplist = []
    mapID = gameBoard.getMapID(fieldID, user["pos"])
    for item in gameBoard.mapEvents[mapID]:
        maplist.append(item["field_card"])

    maplist = list(set(maplist))
    return maplist


def getDeckList(userID):
    list = []
    deck = getDeck(userID)
    for card in deck:
        if card["hand"] == 1:
            list.append(card["card_id"])
    return list


# ---------- Post -------------


def changeField(userID, field):
    userDB.changeField(userID, field)


def processChoices(deck, card, user):
    # check card Event first to find if a action is in the basic
    for event in gameBoard.cardEvents[int(card)]:
        if int(event.get("user_card")) == int(deck):
            return effect.updateUser(user, int(event["result"]), int(event["param"]))

    # check map Event to find if a action is special
    fieldID = gameBoard.getFieldID(user["field"])
    if fieldID == "error":
        return 0

    mapID = gameBoard.getMapID(fieldID, user["pos"])
    for event in gameBoard.mapEvents[mapID]:
        if int(event.get("user_card")) != int(deck):
            continue
        if int(event.get("field_card")) != int(card):
            continue
        return effect.updateUser(user, int(event["result"]), int(event["param"]))

    return 0
