import os
from flask import Flask, request
app = Flask(__name__)
from flask_cors import CORS
CORS(app)
import sqlalchemy
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
import jwt
import requests
import models

def user_create():
    duplicate_user = models.User.query.filter_by(email=request.json["email"]).first()
    if duplicate_user:
        return {"message": "Come on now, there can't be two of you, this email is taken"}, 400
    
    hashed_pw = bcrypt.generate_password_hash(request.json["password"]).decode('utf-8')
    user = models.User(
        name = request.json["name"],
        email = request.json["email"],
        password = hashed_pw
    )
    models.db.session.add(user)
    models.db.session.commit()

    encrypted_id = jwt.encode({"user_id": user.id}, os.environ.get('JWT_SECRET'), algorithm="HS256")
    return {"user": user.to_json(), "user_id": encrypted_id}

def user_login():
    user = models.User.query.filter_by(email=request.json["email"]).first()
    if not user:
        return {"message": "I'm sorry, I can't seem to recall who you are" }, 404
    if bcrypt.check_password_hash(user.password, request.json["password"]):
        encrypted_id = jwt.encode({"user_id": user.id}, os.environ.get('JWT_SECRET'), algorithm="HS256")
        return {"user": user.to_json(), "user_id": encrypted_id }
    else:
        return {"message": "Can't seem to recall your password, eh?"}, 401

def verify_user():
    user = models.User.query.filter_by(id=request.headers["Authorization"]).first()
    if not user:
        return{ "message": "I'm sorry, I can't seem to recall who you are"}, 404
    return {"user": user.to_json() }