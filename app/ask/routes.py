from flask import render_template, redirect, session
from service.userService import getUser
from service.askService import getAskOption
from app.ask import bp


@bp.route('/index',  methods=["GET"])
def index():

    if not session.get("user_id"):
        return redirect("/")
    userID = session.get("user_id")
    user = getUser(userID)
    statut = getAskOption(userID)
    return render_template('game/ask.html', statut=statut, user=user, str=str)
