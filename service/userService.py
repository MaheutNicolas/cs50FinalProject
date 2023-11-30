import dataAcess.userDA as db
from flask import session
import service.deckService as deck


def checkUser(name, password):
    user = db.checkUser(name, password)
    if user == None:
        return False
    session["user_id"] = user["id"]
    return True


def addUser(name, password):
    if db.getUser(name):
        return False

    db.addUser(name, password)
    user = db.getUser(name)[0]
    session["user_id"] = user["id"]

    deck.addCard(user["id"], 1)

    return True


def getUser(userID):
    return db.getUserByID(userID)


def changeLanguage(userID, language):
    db.changeLanguage(userID, language)


def deleteAccount(userID, password):
    if db.checkPassword(userID, password):
        db.removeUser(userID)
        return True
    return False
