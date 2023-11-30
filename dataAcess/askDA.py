import sqlite3
from holder import link as sqlLink


def getAsk():
    connect = sqlite3.connect(sqlLink)
    connect.row_factory = sqlite3.Row
    cursor = connect.cursor()
    cursor.execute(
        "SELECT * FROM ask"
    )
    rows = [dict(row) for row in cursor.fetchall()]
    cursor.close()
    connect.close()
    return rows


def addAskOption(userID, index):
    connect = sqlite3.connect(sqlLink)
    connect.row_factory = sqlite3.Row
    cursor = connect.cursor()
    cursor.execute(
        "INSERT INTO user_ask VALUES (?, ?)", [userID, index]
    )
    connect.commit()
    cursor.close()
    connect.close()


def getAskOption(userID):
    connect = sqlite3.connect(sqlLink)
    connect.row_factory = sqlite3.Row
    cursor = connect.cursor()
    cursor.execute(
        "SELECT * FROM user_ask WHERE user_id = ?", [userID]
    )
    rows = [dict(row) for row in cursor.fetchall()]
    cursor.close()
    connect.close()
    return rows


def verifyAskOption(userID, index):
    connect = sqlite3.connect(sqlLink)
    connect.row_factory = sqlite3.Row
    cursor = connect.cursor()
    cursor.execute(
        "SELECT * FROM user_ask WHERE user_id = ? AND ask_id = ?", [
            userID, index]
    )
    bool = False
    if len(cursor.fetchall()) > 0:
        bool = True
    cursor.close()
    connect.close()
    return bool
