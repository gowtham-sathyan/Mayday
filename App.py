import json
from flask import request
from flask import Flask, jsonify, session, render_template, request, redirect, g, url_for
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
CORS(app, support_credentials=True)

@app.route("/registration", methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        fname=str(data['fname'])
        lname=str(data['lname'])
        pwd=str(data['pwd'])
        email = str(data['email'])
        mobile = str(data['mobile'])
        state = str(data['state'])
        city = str(data['city'])
        print(fname,lname,pwd,email,mobile,state,city)
    return render_template('registration.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)