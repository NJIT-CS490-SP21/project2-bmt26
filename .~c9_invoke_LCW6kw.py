import os
from flask import Flask, send_from_directory, json, session
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__, static_folder='./build/static')
cors = CORS(app, resources={r"/*": {"origins": "*"}})

global userList, xTurn, ticList, ready1, ready2
userList = []
ticList = ['', '', '', '', '', '', '', '', '']
xTurn=True
ready1 = False
ready2 = False

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


@socketio.on('requestLeaderBoard')
def sendLeaderBoard(data): 
    socketio.emit('sentLeaderBoard',  data, broadcast=True, include_self=False)

@socketio.on('clickAttempt')
def on_click(data):
    global xTurn, ticList, ready1, ready2
    success=False
    if((xTurn) and ready1 and ready2 and (ticList[int(data.get('id'))]=='') and (data.get('username')==userList[0])): 
        success=True
        socketio.emit('clickSuccessX', data, broadcast=True, include_self=True)
        ticList[int(data.get('id'))]='X'
        xTurn=not xTurn
    elif((not xTurn) and ready1 and ready2 and (ticList[int(data.get('id'))]=='') and (data.get('username')==userList[1])): 
        success=True
        socketio.emit('clickSuccessO',  data, broadcast=True, include_self=True)
        ticList[int(data.get('id'))]='O'
        xTurn=not xTurn
    else: 
        socketio.emit('clickFailed',  data, broadcast=True, include_self=True)
    
    if success:
        temp = 0
        if(ticList[0]!='' and ticList[0]==ticList[1] and ticList[1]==ticList[2]):
            temp = {'face': ticList[0], 'username': data.get('username')}
            
        elif(ticList[3]!='' and ticList[3]==ticList[4] and ticList[4]==ticList[5]):
            temp = {'face': ticList[3], 'username': data.get('username')}
            
        elif(ticList[6]!='' and ticList[6]==ticList[7] and ticList[7]==ticList[8]):
            temp = {'face': ticList[6], 'username': data.get('username')}
            
        elif(ticList[0]!='' and ticList[0]==ticList[3] and ticList[3]==ticList[6]):
            temp = {'face': ticList[0], 'username': data.get('username')}
            
        elif(ticList[1]!='' and ticList[1]==ticList[4] and ticList[4]==ticList[7]):
            temp = {'face': ticList[1], 'username': data.get('username')}
            
        elif(ticList[2]!='' and ticList[2]==ticList[5] and ticList[5]==ticList[8]):
            temp = {'face': ticList[2], 'username': data.get('username')}
        
        elif(ticList[0]!='' and ticList[0]==ticList[4] and ticList[4]==ticList[8]):
            temp = {'face': ticList[0], 'username': data.get('username')}
        
        elif(ticList[2]!='' and ticList[2]==ticList[4] and ticList[4]==ticList[6]):
            temp = {'face': ticList[2], 'username': data.get('username')}
        
        elif(not ('' in ticList)):
            temp = {'face': '', 'username': data.get('username')}
        
        else:
            success=False
        
        if success==True:
            socketio.emit('gameOver',  temp, broadcast=True, include_self=True)
            temp = {'user0': userList[0], 'user1': userList[1]}
            socketio.emit('playAgainPrompt',  temp, broadcast=True, include_self=True)
            ticList = ['', '', '', '', '', '', '', '', '']
            ready1=False
            ready2=False
            xTurn=True

@socketio.on('playAgainAttempt')
def playAgainAttempt(username) :
    global ready1, ready2
    if len(userList)>=2 :
        if userList[0] == username.get('username') :
            if not ready1:
                ready1 = True
            else :
                ready2 = True
            socketio.emit('playAgainSuccess', username, broadcast=False, include_self=True)
        elif userList[1] == username.get('username') :
            if not ready2:
                ready2 = True
            else :
                ready1 = True
            socketio.emit('playAgainSuccess', username, broadcast=False, include_self=True)
        else:
            socketio.emit('playAgainFailed', username, broadcast=False, include_self=True)
    else:
        socketio.emit('playAgainFailed', username, broadcast=False, include_self=True)
        
@socketio.on('notAgainAttempt')
def notAgainAttempt(username) :
    global ready1, ready2
    if len(userList)>=2 and ( userList[0]==username.get('username') or userList[1]==username.get('username') ) : 
        if userList[0] == username.get('username') :
            if not ready1:
                ready1 = True
            else :
                ready2 = True
        elif userList[1] == username.get('username') : 
            if not ready2:
                ready2 = True
            else :
                ready1 = True
        userList.remove(username.get('username'))
        userList.append(username.get('username'))
        socketio.emit('notAgainSuccess',  username, broadcast=False, include_self=True)
        socketio.emit('userList',  userList, broadcast=True, include_self=True)
        
        
    else:
        socketio.emit('notAgainFailed', username, broadcast=False, include_self=True)


@socketio.on('loginAttempt')
def loginAttempt(username):
    global ready1, ready2
    if not (username.get('username') in userList): 
        userList.append(username.get('username'))
        socketio.emit('loginSuccess',  username, broadcast=False, include_self=True)
        socketio.emit('userList',  userList, broadcast=True, include_self=True)
        if len(userList)==1 :
            ready1 = True
        elif len(userList)==2 :
            ready2 = True
        
    else:
        socketio.emit('loginFailed', username, broadcast=False, include_self=True)

@socketio.on('logoutAttempt')
def logoutAttempt(username):
    global ready1, ready2
    if (username.get('username') in userList): 
        userList.remove(username.get('username'))
        socketio.emit('logoutSuccess',  username, broadcast=True, include_self=True)
        socketio.emit('userList',  userList, broadcast=True, include_self=True)
        if len(userList)==0 :
            ready1 = False
        elif len(userList)==1 :
            ready2 = False
    else:
        socketio.emit('logoutFailed', username, broadcast=False, include_self=True)


# Note that we don't call app.run anymore. We call socketio.run with app arg
socketio.run(
    app,
    host=os.getenv('IP', '0.0.0.0'),
    port=8081 if os.getenv('C9_PORT') else int(os.getenv('PORT', 8081)),
);