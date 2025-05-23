from flask import Flask, request,render_template
app = Flask(__name__)
studentDB = {
                1: {
                        "id": 1,
                        "name": "sayantan",
                        "mob": 9829111123,
                        "courses": ["QC", "AI"]
                },

                2: { 
                        "id": 2,
                        "name": "eric",
                        "mob": 9829122222,
                        "courses": ["AI"]
                },

                3:  {
                        "id": 3,
                        "name": "tom",
                        "mob": 9829133333,
                        "courses": ["Full Stack"]
                }        
}

@app.route("/", methods=['GET'])
def lwhome():
    return "Welcome to LW Students DB.. <a href ='/students'> Check All Records </a>"

@app.route("/students", methods=['GET'])
def lwstudentsinfo():
    return render_template("students_entire_info.html", db=studentDB)

@app.route("/student/<int:index>", methods=['GET'])
def lwstudentinfo(index):
    if index <= 0:
        return "Not exists"
    elif index in list(studentDB.keys()):
        return render_template( 
                                "studentinfo.html",
                                stName = studentDB[int(index)]['name'],
                                stMob = studentDB[int(index)]['mob'],
                                stCourses = studentDB[int(index)]['courses'],
                                stID = studentDB[int(index)]['id']
                            )
    else:
        return "Not exists"

@app.route("/student/create", methods=['POST'])
def lwstudentcreate():
    if len(studentDB): # if record is not empty
        studentDB[list(studentDB.keys())[-1] + 1] = request.json # map the record with the key 
        # that is 1 greater than  the highest exisiting key 
        # studentDB[max(studentDB.keys()) + 1] = request.json 
    else: # if record is empty 
        studentDB[1] = request.json # store this as first record and map it with key '1'
    return "record created .."

@app.route("/student/delete/<int:index>", methods=['DELETE'])
def lwstudentdelete(index):
    del studentDB[ index ]
    return "record deleted .."

app.run()