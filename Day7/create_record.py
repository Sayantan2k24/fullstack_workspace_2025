from flask import Flask, request

app = Flask(__name__)

studentDB = []

@app.route("/", methods=['GET'])
def lwhome():
    return "Welcome to LW Student DB"

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
    
@app.route("/student/create", methods=['POST'])
def lwstudentcreate():
    print("method: ", request.method)
    print("data: ", request.json)

    studentDB.append(request.json)
    return "record created"

@app.route("/student/delete/<index>", methods=['DELETE'])
def lwstudentdelete(index):
    studentDB.remove( studentDB[int(index) -1 ] )
    return "record deleted .."


app.run()
