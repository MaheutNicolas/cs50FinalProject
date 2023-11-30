import sqlite3
from holder import link as sqlLink


def getMap():

    connect = sqlite3.connect(sqlLink)
    connect.row_factory = sqlite3.Row
    cursor = connect.cursor()
    cursor.execute(
        "SELECT * FROM maps"
    )
    rows = [dict(row) for row in cursor.fetchall()]
    cursor.close()
    connect.close()

    connect = sqlite3.connect(sqlLink)
    connect.row_factory = sqlite3.Row
    cursor = connect.cursor()
    cursor.execute(
        "SELECT * FROM map_events"
    )
    holder = [dict(row) for row in cursor.fetchall()]
    cursor.close()
    connect.close()

    maxLength = 0
    for event in holder:
        if maxLength < event["map_id"]:
            maxLength = event["map_id"]

    mapEvent = []  # first index Empty to pass list to base 1

    for num in range(maxLength):
        mapEvent.append([])
    mapEvent.append([])

    for event in holder:
        index = event["map_id"]
        del event["map_id"]
        mapEvent[index].append(event)

    return [rows, mapEvent]
