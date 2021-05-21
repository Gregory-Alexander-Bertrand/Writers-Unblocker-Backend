from flask import request
import models

def user_create():
    user = models.User(
        name=request.json["name"],
        email=request.json["email"],
        password=request.json["password"]
    )
    models.db.session.add(user)
    models.db.session.commit()
    return 'okay'

def user_login():
    user = models.User.query.filter_by(email=request.json["email"]).first()
    if not user:
        return {"message": "I'm sorry, I can't seem to recall who you are" }, 404
    if user.password == request.json["password"]:
        return {"user": user.to_json() }
    else:
        return {"message": "Can't seem to recall your password, eh?"}, 401