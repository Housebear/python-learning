#!/usr/bin/python3
# -*- coding:utf-8 -*-

# File Name: app.py
# Author: Lipsum
# Mail: niuleipeng@gmail.com
# Created Time: 2016-05-16 18:09:55

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def sign_form():
    return '''<form action="/signin" method="post">
            <p><input name="username"></p>
            <p><input name="password" type="password"></p>
            <p><button type="submit">Sign in</button></p>
            </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello admin</h3>'
    return '<h3>Bad username or password</h3>'

if __name__ == '__main__':
    app.run()


