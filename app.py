from flask import Flask
app = Flask(__name__)
from flask import request,  send_from_directory

@app.route('/subscribe', methods=['POST'])
def subscribe():
    print(request.form["email"] )
    f = open("emails.txt", "a")
    f.write(request.form["email"] + "\n")
    f.close()
    return "Ok"

@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/')
def send_index():
    return send_from_directory('static', "index.html")