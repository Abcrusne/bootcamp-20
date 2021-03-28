import os

from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit
from collections import deque

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


users = {}

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on('message')
def message(data):
    print(f"\n {data} \n")
    send({'msg': data['msg'], 'username' : data['username']}, broadcast = True)

@socketio.on('new username')
def new_username(data):
    username = ""
    users[data['username']]=request.sid
    print(users)
    username = data['username']
    # username=data["username"]
    # print(username)
    emit("add username", {"username":username})

if __name__ == '__main__':
    socketio.run(app, debug=True, use_reloader=True)
