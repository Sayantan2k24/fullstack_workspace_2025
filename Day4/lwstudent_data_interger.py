from flask import Flask
app = Flask(__name__)

@app.route("/")
def lwinfo():
    return "Linux World ... Info"

# @app.route("/data")
# def lwdata():
#     return 10

@app.route("/data")
def lwdata():
    return str(10)

app.run()


