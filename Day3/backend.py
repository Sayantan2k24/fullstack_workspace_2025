from flask import Flask
app = Flask(__name__)

@app.route("/search")
def mysearch():
    return "i m have done searching ...\n"

@app.route("/mail")
def myemail():
    sreturn "<b> i do email...</b><br /> hi hello <br /> User <input />
app.run()