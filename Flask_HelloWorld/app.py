from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello() -> str:
    return "Hello, World!"

app.run(host="0.0.0.0")