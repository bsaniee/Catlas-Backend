from flask import Flask

## Import SQL alchemy and os

from flask_sqlalchemy import SQLAlchemy
import os


## Create application Object

app = Flask(__name__)
## app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

## Routes

@app.get("/")
def home():
    return {"response": "Hello World"}

app.run(host="localhost", port=3000)