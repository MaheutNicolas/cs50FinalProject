from flask import render_template, session, redirect, request
from app.deck import bp
from service.userService import getUser
import service.deckService as deck


@bp.route('/index',  methods=["GET", "POST"])
def index():
    if not session.get("user_id"):
        return redirect("/")
    userID = session.get("user_id")

    if request.method == "GET":
        user = getUser(userID)
        statut = deck.getDeckStatut(user)
        return render_template("/game/deck.html", statut=statut)
    else:
        deck.switchCardInHand(request.form.get("id"), userID)
        return redirect("/deck/index")
