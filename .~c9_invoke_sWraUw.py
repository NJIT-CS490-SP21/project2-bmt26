import os
from flask import Flask, send_from_directory, json, session
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__, static_folder='./build/static')
cors = CORS(app, resources={r"/*": {"origins": "*"}})
userList = []
ticList = ['', '', '', '', '', '', '', '', '']

global xTurn
xTurn=True

def checkWin():
    if(ticList[0]==ticList[1] and ticList[1]==ticList[2]):
        
    elif(ticList[3]==ticList[4] and ticList[4]==ticList[5]):
        
    elif(ticList[6]==ticList[7] and ticList[7]==ticList[8]):
        
    elif(ticList[0]==ticList[3] and ticList[3]==ticList[6]):
        
    elif(ticList[1]==ticList[4] and ticList[4]==ticList[7]):
        
    elif(ticList[2]==ticList[5] and ticList[5]==ticList[8]):
        
    elif(ticList[0]==ticList[4] and ticList[4]==ticList[8]):
        
    elif(ticList[2]==ticList[4] and ticList[4]==ticList[6]):
        
def alertWin():
    socketio.emit('win',  face:X, broadcast=True, include_self=True)

socketio = SocketIO(
    app,
    cors_allowed_origins="*",
    json=json,
    manage_session=False
)

@app.route('/', defaults={"filename": "index.html"})
@app.route('/<path:filename>')
def index(filename):
    return send_from_directory('./build', filename)

# When a client connects from this Socket connection, this function is run
@socketio.on('connect')
def on_connect():
    print('User connected!')

# When a client disconnects from this Socket connection, this function is run
@socketio.on('disconnect')
def on_disconnect():
    print('User disconnected!')

@socketio.on('chat')
def on_chat(data): 
    socketio.emit('chat',  data, broadcast=True, include_self=False)

@socketio.on('clickAttempt')
def on_click(data):
    global xTurn
    if((data.get('username')==userList[0]) and (xTurn)): 
        socketio.emit('clickSuccessX', data, broadcast=True, include_self=True)
        ticList[data.id]='X'
        xTurn=not xTurn
    elif((data.get('username')==userList[1]) and (not xTurn)): 
        socketio.emit('clickSuccessO',  data, broadcast=True, include_self=True)
        ticTList[data.id]='O'
        xTurn=not xTurn
    else: 
        socketio.emit('clickFailed',  data, broadcast=True, include_self=True)
    

@socketio.on('loginAttempt')
def loginAttempt(username):
    if not (username.get('username') in userList): 
        userList.append(username.get('username'))
        socketio.emit('loginSuccess',  username, broadcast=False, include_self=True)
        
    else:
        socketio.emit('loginFailed', username, broadcast=False, include_self=True)

@socketio.on('logoutAttempt')
def logoutAttempt(username):
    if (username.get('username') in userList): 
        userList.remove(username.get('username'))
        socketio.emit('logoutSuccess',  username, broadcast=True, include_self=True)
    else:
        socketio.emit('logoutFailed', username, broadcast=False, include_self=True)


# Note that we don't call app.run anymore. We call socketio.run with app arg
socketio.run(
    app,
    host=os.getenv('IP', '0.0.0.0'),
    port=8081 if os.getenv('C9_PORT') else int(os.getenv('PORT', 8081)),
);