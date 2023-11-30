import sqlite3
from holder import link as sqlLink


def getCardEvent():

    connect = sqlite3.connect(sqlLink)
    connect.row_factory = sqlite3.Row
    cursor = connect.cursor()
    cursor.execute(
        "SELECT * FROM card_events"
    )
    holder = [dict(row) for row in cursor.fetchall()]
    cursor.close()
    connect.close()

    maxLength = 0
    for event in holder:
        if maxLength < event["field_card"]:
            maxLength = event["field_card"]

    cardEvent = []
    cardEvent.append([])  # first index Empty to pass list to base 1
    for num in range(maxLength):
        cardEvent.append([])

    for event in holder:
        index = event["field_card"]
        del event["field_card"]
        cardEvent[index].append(event)

    return cardEvent
