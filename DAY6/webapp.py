from flask import Flask, render_template, request 
app = Flask(__name__) 

@app.route("/", methods=['GET']) 
def home(): 
    return render_template("mydata.html") 

@app.route("/lw", methods = ['POST']) 
def lw(): 
    # get data from client using GET queryString
    # data = request.args.get("x") 

    #get data from client using POST method
    data = request.form["x"]
    return f"welcome to {data}"

app.run() 
