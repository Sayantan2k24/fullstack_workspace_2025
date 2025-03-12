from flask import Flask
app = Flask(__name__)

@app.route("/info")
def lwinfo():
    return "Linux World ... Info"

# @app.route("/student/<name>")
# def lwstudent(name):
#     return f"this is {name} student"

@app.route("/student/<name>/<city>")
def lwstudentinfo(name,city):
    return f"this is <b>{name}</b> student from city <u>{city}</u>"

# @app.route("/sms/<phone>/<msg>")
# def send_message(phone, msg):
#     return f"phone number: {phone} Sent Message: {msg}"

app.run()
