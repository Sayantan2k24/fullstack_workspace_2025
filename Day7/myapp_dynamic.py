from flask import Flask

app = Flask(__name__)

studentDB = [
    {
        "id": 1,
        "name": "vimal",
        "mob": 9829111123,
        "courses": ["QC", "AI"]
    },
    {
        "id": 2,
        "name": "eric",
        "mob": 9829122222,
        "courses": ["AI"]
    },
    {
        "id": 3,
        "name": "tom",
        "mob": 9829133333,
        "courses": ["Full Stack"]
    }
]

@app.route("/", methods=['GET'])
def lwhome():
    return { "data":"i am home page"}

@app.route("/students", methods=['GET'])
def lwstudentsinfo():
    return studentDB

@app.route("/student/<index>", methods=['GET'])
def lwstudentinfo(index):
    if int(index) <= 0:
        return "Not exists"
    elif len(studentDB) >= int(index):
        return studentDB[int(index) - 1]
    else:
        return "Not exist"

app.run()
