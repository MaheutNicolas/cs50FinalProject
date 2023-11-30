from dataAcess.gameBoardDA import get
from dataAcess.mapDA import getMap
from dataAcess.cardEventDA import getCardEvent
import sys

cards = []
fields = []
maps = []
mapEvents = []
cardEvents = []


def init():
    global cards
    cards = get("cards")

    global fields
    fields = get("fields")

    global maps
    global mapEvents
    maps, mapEvents = getMap()

    global cardEvents
    cardEvents = getCardEvent()


def getFieldName(id):
    return fields[id]["name"]


def getFieldID(name):
    for field in fields:
        if name == field["name"]:
            return field["id"]

    return "error"


def getMapID(fieldID, pos):

    if fieldID == "error":
        return "error"

    for map in maps:
        if map["field_id"] == fieldID and map["number"] == pos:
            return map["id"]
