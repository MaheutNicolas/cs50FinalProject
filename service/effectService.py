import dataAcess.userDA as userDB
import service.deckService as deck
import service.askService as askDB
import gameBoard


def updateUser(user, result, param):
    match result:
        # the player move up (pass by 5 maps because the grid is 5*5)
        case 1:
            transition = user["pos"] - ((param * 5) % 25)
            if transition < 1:
                transition = 25 + transition
            userDB.changePos(user["id"], transition)
            return 1
        # the player move down (pass by 5 maps because the grid is 5*5)
        case 2:
            transition = (user["pos"] + (param * 5)) % 25
            userDB.changePos(user["id"], transition)
            return 1
        # the player move right
        case 3:
            rowPos = user["pos"] % 5  # pos initial in the row
            if rowPos == 0:  # gard against 0 for the calc of "pos"
                rowPos = 5
            # add param to obtain the new pos
            transition = rowPos + (param % 5)
            # if True comeback to the beginning of the row (can't be more than 9 because of the %)
            if transition > 5:
                transition = transition - 5
            pos = user["pos"] - rowPos + transition
            userDB.changePos(user["id"], pos)
            return 1
        # the player move left
        case 4:
            rowPos = user["pos"] % 5  # user pos in the row
            # the number of map from the beginning of the row
            if rowPos == 0:
                rowPos = 5
            transition = rowPos - (param % 5)
            if transition < 1:
                transition = 5 + transition
            # user start to the beginning ( user["pos"] - rowPos) and travel to the number in Transition
            transition = user["pos"] - rowPos + transition
            userDB.changePos(user["id"], transition)
            return 1
        # switch Field
        case 5:
            userDB.changeField(user["id"], gameBoard.getFieldName(param))
            return 2
        # return Lobby
        case 6:
            userDB.changeField(user["id"], "lobby")
            return 1
        # add Card to deck (check if the function can place it in hand)
        case 7:
            return deck.addCard(user["id"], param)
        # switch to the "param" pos
        case 8:
            userDB.changePos(user["id"], param)
            return 1
        # add dialogue option
        case 9:
            return askDB.addAskOption(user["id"], param)
        # Victory
        case 10:
            userDB.changeField(user["id"], "victory")
            return 1
        case _:
            return 0
