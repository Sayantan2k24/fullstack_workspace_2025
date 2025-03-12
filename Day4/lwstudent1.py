from flask import Flask
app = Flask(__name__)

@app.route("/info")
def lwinfo():
    return "Linux World ... Info"


@app.route("/student/abhi")
def lwstudentinfo1():
    return "this is abhi student1"

@app.route("/student/tom")
def lwstudentinfo2():
    return "this is tom student2"

app.run()


