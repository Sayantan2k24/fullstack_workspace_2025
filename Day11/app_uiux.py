from flask import Flask, request,render_template
app = Flask(__name__)
studentDB = {
                1: {
                        "id": 1,
                        "name": "sayantan",
                        "mobile": 9829111123,
                        "courses": ["QC", "AI"]
                },

                2: { 
                        "id": 2,
                        "name": "eric",
                        "mobile": 9829122222,
                        "courses": ["AI"]
                },

                3:  {
                        "id": 3,
                        "name": "tom",
                        "mobile": 9829133333,
                        "courses": ["Full Stack"]
                }         
}

@app.route("/", methods=['GET'])
def lwhome():
    return render_template("myhome.html")

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
                                stmob = studentDB[int(index)]['mobile'],
                                stCourses = studentDB[int(index)]['courses'],
                                stID = studentDB[int(index)]['id']
                            )
    else:
        return "Not exists"

@app.route("/student/create", methods=['POST'])
def lwstudentcreate():

    # print(request.files)

    
    fh = request.files['myfile']
    print(fh)

    if fh.mimetype == 'image/jpeg':

        fh.save(f"templates/{fh.filename}")
    else: 
        print("file type not supported")

    print(dir(fh))

    print( fh.content_length, fh.filename, fh.mimetype, fh.name)

    if request.form:
        # print("FORM: ", request.form)
        result = request.form
        # print(result)

        name = result['name']
        mobile = result['mobile']
        courses = result['courses']

        # print(result['myfile'])

        if len(studentDB): # if record is not empty
            # nextId = list(studentDB.keys())[-1] + 1
            nextId = max(studentDB.keys()) + 1

            studentDB[nextId] = {
                "id": nextId,
                "name": name,
                "mobile": mobile,
                "courses": [courses]    
            }

        else: # if record is empty
            # add the first record --> index 1
            studentDB[1] = {
                "id": 1,
                "name": name,
                "mobile": mobile,
                "courses": [courses]    
            }
        
        return "record created .."

    elif request.json:
        # print("JSON: ", request.json)
        if len(studentDB): # if record is not empty
            # studentDB[list(studentDB.keys())[-1] + 1] = request.json # map the record with the key 
            # that is 1 greater than  the highest exisiting key 
            studentDB[max(studentDB.keys()) + 1] = request.json 
        else: # if record is empty 
            studentDB[1] = request.json
             # store this as first record and map it with key '1'
        
        return "record created .." # common for both if and else

    else:
        return "not supported"


@app.route("/student/delete/<int:index>", methods=['DELETE'])
def lwstudentdelete(index):
    del studentDB[ index ]
    return "record deleted .."

@app.route("/student/update/<item>/<index>", methods=['PATCH'])
def lwstudentpatch(item, index):
    # print(request.json)
    data  = request.json

    # if 'mobile' == item:
        # item = 'mob'

    if item in data and item in studentDB[int(index)]:
        print(data[item])
        studentDB[int(index)][item] = data[item]
        
        return f"Success: key: {item} in record {int(index)} patched.."
    else:
        return f"Error: key: {item} does not exist .. to patch"
    
#PUT
@app.route("/student/updates/<index>", methods=['PUT'])
def lwstudentput(index):
    data = request.json

    if int(index) in studentDB:

        # studentDB[int(index)] = data
        studentDB[int(index)] = {
                "id": int(index),
                "name": data['name'],
                "mobile" : data['mobile'],
                "courses": data['courses']
        }

        return f"Success: Entire record {index} updated"
    else:
        return f"Error: id : {index} does not exist"


app.run()