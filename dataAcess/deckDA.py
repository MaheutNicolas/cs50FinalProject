import sqlite3
from holder import link as sqlLink


def getDeck(userID):
    connect = sqlite3.connect(sqlLink)
    connect.row_factory = sqlite3.Row
    cursor = connect.cursor()
    cursor.execute(
        "SELECT * FROM deck WHERE user_id = ?", [userID]
    )
    rows = [dict(row) for row in cursor.fetchall()]
    cursor.close()
    connect.close()
    return rows


def addCardInDB(userID, cardID, hand):
    connect = sqlite3.connect(sqlLink)
    connect.row_factory = sqlite3.Row
    cursor = connect.cursor()
    cursor.execute(
        "INSERT INTO deck VALUES (?, ?, ?)", [userID, cardID, hand]
    )
    connect.commit()
    cursor.close()
    connect.close()


def getDeckWithCard(userID):
    connect = sqlite3.connect(sqlLink)
    connect.row_factory = sqlite3.Row
    cursor = connect.cursor()
    cursor.execute(
        "SELECT * FROM deck INNER JOIN cards ON deck.card_id = cards.id WHERE user_id = ?", [
            userID]
    )
    rows = [dict(row) for row in cursor.fetchall()]
    cursor.close()
    connect.close()
    return rows


def switchValueInHand(cardID, userID):
    connect = sqlite3.connect(sqlLink)
    connect.row_factory = sqlite3.Row
    cursor = connect.cursor()
    cursor.execute(
        "UPDATE deck SET hand = ((hand - 1) * -1) WHERE user_id = ? AND card_id = ?", [
            userID, cardID]
    )
    connect.commit()
    cursor.close()
    connect.close()


def checkHandCapacityInDB(userID):
    connect = sqlite3.connect(sqlLink)
    connect.row_factory = sqlite3.Row
    cursor = connect.cursor()
    cursor.execute(
        "SELECT COUNT(*) FROM deck WHERE user_id = ? AND hand = 1", [userID]
    )
    row = [list(row) for row in cursor.fetchall()][0][0]
    cursor.close()
    connect.close()
    return row


def isCardAlreadyUnlock(userID, cardID):
    connect = sqlite3.connect(sqlLink)
    connect.row_factory = sqlite3.Row
    cursor = connect.cursor()
    cursor.execute(
        "SELECT * FROM deck WHERE user_id = ? AND card_id = ?", [
            userID, cardID]
    )
    bool = False
    if len(cursor.fetchall()) > 0:
        bool = True
    cursor.close()
    connect.close()
    return bool
