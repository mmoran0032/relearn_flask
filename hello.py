#!/usr/bin/env python3


from flask import Flask, make_response, request
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return make_response('<h1>Hello, Laura!</h1>'
                         f'<p>Your browser is {user_agent}</p>')


@app.route('/user/<name>')
def user(name):
    return make_response(f'<h1>Hello, {name}!</h1>')


if __name__ == '__main__':
    manager.run()
