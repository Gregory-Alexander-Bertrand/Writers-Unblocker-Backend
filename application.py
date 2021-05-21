import os
from dotenv import load_dotenv
from flask import Flask, request
import sqlalchemy

import models
from routes import apply_routes

load_dotenv()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL')
models.db.init_app(app)

def root():
    return {"message": "okay" }
app.route('/', methods=["GET"])(root)

apply_routes(app)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)