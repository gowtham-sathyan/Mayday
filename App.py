import pymongo
from pymongo import MongoClient
import json
from flask import request
from flask import Flask, jsonify, session, render_template, request, redirect, g, url_for
from flask_cors import CORS, cross_origin
import os

client = MongoClient('localhost')
db = client.Disaster
collection = db.Users
app = Flask(__name__)
app.secret_key = os.urandom(24)
CORS(app, support_credentials=True)


@app.route("/registration", methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        fname = str(data['fname'])
        lname = str(data['lname'])
        pwd = str(data['pwd'])
        email = str(data['email'])
        mobile = str(data['mobile'])
        state = str(data['state'])
        city = str(data['city'])
        post = {"fname": fname, "lname": lname, "password": pwd, "email": email, "mobile": mobile, "state": state,
                "city": city}
        posts = db.posts
        post_id = collection.insert_one(post).inserted_id
        return render_template('login.html')
    return render_template('registration.html')


@app.route("/login", methods=['POST', 'GET'])
def login():
    error = ''
    if request.method == 'POST':
        session.pop('user', None)
        data = request.get_json()
        print(data)
        email = str(data['email'])
        pwd = str(data['pwd'])
        print(pwd, email)
        # if user exists then session['user'] = request.form['email'] else return render_template('login.html', error='Invalid Credentials!')
    return render_template('login.html', error='')

@app.before_request
def bef_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
