from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
from holder import link as sqlLink


def checkUser(name, password):
    connect = sqlite3.connect(sqlLink)
    connect.row_factory = sqlite3.Row
    cursor = connect.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE name = ?", [name]
    )
    row = [dict(row) for row in cursor.fetchall()]
    cursor.close()
    connect.close()

    # Ensure username exists and password is correct
    if len(row) != 1 or not check_password_hash(
        row[0]["password"], password
    ):
        return None
    return row[0]


def checkPassword(userId, password):
    connect = sqlite3.connect(sqlLink)
    connect.row_factory = sqlite3.Row
    cursor = connect.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE id = ?", [userId]
    )
    row = [dict(row) for row in cursor.fetchall()]
    cursor.close()
    connect.close()

    # Ensure username exists and password is correct
    if len(row) != 1 or not check_password_hash(
        row[0]["password"], password
    ):
        return False
    return True


def getUser(name):
    connect = sqlite3.connect(sqlLink)
    connect.row_factory = sqlite3.Row
    cursor = connect.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE name = ?", [name]
    )
    row = [dict(row) for row in cursor.fetchall()]
    cursor.close()
    connect.close()
    return row


def getUserByID(id):
    connect = sqlite3.connect(sqlLink)
    connect.row_factory = sqlite3.Row
    cursor = connect.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE id = ?", [id]
    )
    row = [dict(row) for row in cursor.fetchall()][0]
    cursor.close()
    connect.close()
    return row


def addUser(name, password):
    connect = sqlite3.connect(sqlLink)
    cursor = connect.cursor()
    cursor.execute(
        "INSERT INTO users (name, password) VALUES (?, ?)", [
            name, encrypt(password)]
    )
    connect.commit()
    cursor.close()
    connect.close()


def removeUser(id):
    connect = sqlite3.connect(sqlLink)
    cursor = connect.cursor()
    cursor.execute(
        "DELETE FROM users WHERE id = ?", [id]
    )
    connect.commit()
    cursor.execute(
        "DELETE FROM deck WHERE user_id = ?", [id]
    )
    connect.commit()
    cursor.execute(
        "DELETE FROM user_ask WHERE user_id = ?", [id]
    )
    connect.commit()
    cursor.close()
    connect.close()


def encrypt(password):
    password = generate_password_hash(
        password, method="pbkdf2", salt_length=16)
    return password


def changeField(userID, field):
    connect = sqlite3.connect(sqlLink)
    cursor = connect.cursor()
    cursor.execute(
        "UPDATE users SET field = ?, pos = 1 WHERE id = ?", [field, userID]
    )
    connect.commit()
    cursor.close()
    connect.close()


def changePos(userID, pos):
    connect = sqlite3.connect(sqlLink)
    cursor = connect.cursor()
    cursor.execute(
        "UPDATE users SET pos = ? WHERE id = ?", [pos, userID]
    )
    connect.commit()
    cursor.close()
    connect.close()


def changeLanguage(userID, language):
    connect = sqlite3.connect(sqlLink)
    cursor = connect.cursor()
    cursor.execute(
        "UPDATE users SET language = ? WHERE id = ?", [language, userID]
    )
    connect.commit()
    cursor.close()
    connect.close()
    return
