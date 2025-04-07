from flask import Flask
app = Flask(__name__)

@app.route("/")
def lwinfo():
    return "Linux World ... Info"

# @app.route("/data")
# def lwdata():
#     return 10 # this will give Internal Server Error

@app.route("/data")
def lwdata():
    return str(10)

app.run()


