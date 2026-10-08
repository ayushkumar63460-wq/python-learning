from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
    return{"message": "Hello from my API!"}

@app.route("/about")
def about():
    return{"name": "Tyler Durden",
           "message": "Rule no:1...",
           }

@app.route("/status")
def status():
    return{"status": "Running!"}


app.run()

