from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['GET'])
def lwhome():
    return "i am home page"

app.run()
