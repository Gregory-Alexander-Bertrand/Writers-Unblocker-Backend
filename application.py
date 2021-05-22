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


app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL')
import models
from dotenv import load_dotenv
load_dotenv()
from routes import apply_routes






models.db.init_app(app)

def root():
    return {"message": "okay" }
app.route('/', methods=["GET"])(root)

apply_routes(app)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)