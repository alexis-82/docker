
from flask import Flask, render_template, make_response, jsonify, request

app=Flask(__name__)

PORT = 3200
HOST = '0.0.0.0'

@app.route("/")
def hello_world():
    # return "<h1 style='color:red'> This is Home!</h1>"
    return render_template('index.html')

if __name__ == "__main__":
    print("Server running in port %s"%(PORT))
    app.run(host='0.0.0.0', port = PORT)