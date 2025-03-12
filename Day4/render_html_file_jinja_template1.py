from flask import Flask, render_template
app = Flask(__name__)

@app.route("/info")
def lwinfo():
    return "Linux World ... Info"

@app.route("/student/<name>")
def lwstudent(name):
    return f"this is {name} student"

@app.route("/student/<name>/<city>")
def lwstudentinfo(name,city):
    return render_template("my_template1.html", x="hi", n=name, c=city)

@app.route("/sms/<phone>/<msg>")
def send_message(phone, msg):
    return f"phone number: {phone} Sent Message: {msg}"

@app.route("/data")
def lwdata():
    return str(10)

app.run()
