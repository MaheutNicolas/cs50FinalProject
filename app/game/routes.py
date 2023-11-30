from flask import render_template, request, session, redirect, jsonify
from service.gameService import getStatut, changeField, processChoices
from service.userService import getUser
from app.game import bp
import language.text as text
import sys


@bp.route('/index',  methods=["GET", "POST"])
def index():

    if not session.get("user_id"):
        return redirect("/")
    userID = session.get("user_id")

    if request.method == "GET":
        user = getUser(userID)
        statut = getStatut(user)
        if statut["field"] == "lobby":
            return render_template('game/lobby.html', statut=statut)
        if statut["field"] == "victory":
            return render_template('game/victory.html', statut=statut)
        if statut["cards"] == "error":
            return render_template('game/lobby.html', statut=statut)

        return render_template('game/board.html', statut=statut)
    else:
        if request.form.get("field"):
            changeField(userID, request.form.get("field"))
            return redirect("/game/index")
        else:
            user = getUser(userID)
            # 0 : fail / 1 : succes without message / 2 : change field / 3 : add card / 4 : add dialogue option / 5 : Effect Already optain
            response = processChoices(
                request.json["deck"], request.json["card"], user)
            if response == 2:
                response = text.get(user["language"], 30)
            if response == 3:
                response = text.get(user["language"], 31)
            if response == 4:
                response = text.get(user["language"], 32)
            if response == 5:
                response = text.get(user["language"], 33)

            data = {
                "response": str(response),
            }

            return jsonify(data)
