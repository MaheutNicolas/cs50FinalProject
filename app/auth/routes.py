from flask import render_template, request, redirect, session
from service.userService import checkUser, addUser, deleteAccount
from app.auth import bp


@bp.route('/login',  methods=["GET", "POST"])
def index():

    if session.get('user_id'):
        return redirect("/")

    if request.method == "POST":

        if not checkUser(request.form.get(
                "name"), request.form.get("password")):
            return render_template('home/login.html', errorMessage="User not found")

        return redirect("/")

    else:
        return render_template('home/login.html',  errorMessage="")


@bp.route('/create',  methods=["GET", "POST"])
def create():

    if session.get('user_id'):
        return redirect("/")

    if request.method == "POST":
        if not addUser(request.form.get("name"), request.form.get("password")):
            return render_template('home/create.html', errorMessage="User not create")

        return redirect("/")

    else:
        return render_template('home/create.html', errorMessage="")


@bp.route('/logout',  methods=["POST"])
def logout():
    if session.get('user_id'):
        session.pop('logged_in', None)
        session.pop("user_id", None)

    return redirect("/")


@bp.route('/delete',  methods=["POST"])
def delete():
    if session.get('user_id'):
        if deleteAccount(session.get('user_id'), request.form.get("password")):
            session.pop('logged_in', None)
            session.pop("user_id", None)
            return redirect("/")
        return redirect("/game/index")
