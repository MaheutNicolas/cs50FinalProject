from flask import render_template, session, redirect, request
from app.main import bp
import service.userService as user
import language.text as text


@bp.route('/')
def index():
    if not session.get("user_id"):
        lang = "eng"
        if "language" in request.args:
            lang = request.args["language"]
        langList = text.getLanguage()
        return render_template('home/index.html', lang=lang, langList=langList)

    return redirect("/game/index")


@bp.route('/language',  methods=["POST"])
def postLanguage():
    if not session.get("user_id"):
        return render_template('home/index.html')
    userID = session.get("user_id")
    user.changeLanguage(userID, request.form.get("language"))

    return redirect("/game/index")
