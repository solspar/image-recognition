from flask import Flask, escape, request
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


@socketio.on('connect')
def handle_connect():
  print('connected')


@socketio.on('message')
def handle_message(message):
  send('hello')
  print('recieved message: ' + message)

if __name__ == '__main__':
  socketio.run(app)
