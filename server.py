from flask import Flask

## Create application Object

app = Flask(__name__)

@app.get("/")
def home():
    return {"response": "Hello World"}

app.run(host="localhost", port=3000)