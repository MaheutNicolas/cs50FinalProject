import sqlite3
from holder import link as sqlLink


def get(table):
    connect = sqlite3.connect(sqlLink)
    connect.row_factory = sqlite3.Row
    cursor = connect.cursor()
    cursor.execute(
        "SELECT * FROM " + table
    )
    rows = [dict(row) for row in cursor.fetchall()]
    cursor.close()
    connect.close()
    return rows
