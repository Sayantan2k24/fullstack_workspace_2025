from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def lw():
    return render_template("index.html")

@app.route("/home", methods=['POST'])
def lwhome1():
    print("i am server.. i am print.. \n")
    print("client requested with this method: ", request.method , "\n")
    data = request.form['n']
    print("data comes from client: ", data , "\n")
    return f"Welcome to LW from POST, I am getting data named {data} \n"

@app.route("/home", methods=['GET'])
def lwhome2():
    print("i am server.. i am print.. \n")
    print("client requested with this method: ", request.method , "\n")
    return "Welcome to LW from GET...\n"

app.run()


