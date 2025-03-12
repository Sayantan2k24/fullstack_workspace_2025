from flask import Flask

app = Flask(__name__)

@app.route("/lw", methods=['GET'])
def lw():
    return "welcome to LW.."

app.run()

