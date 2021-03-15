"""Server For TicTacToe Game"""
import os
from flask import Flask, send_from_directory, json, session
from dotenv import load_dotenv, find_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_socketio import SocketIO

load_dotenv(find_dotenv())  # This is to load your env variables from .env

APP = Flask(__name__, static_folder='./build/static')
APP.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

global USERLIST, XTURN, TICLIST, READY1, READY2, DB
DB = SQLAlchemy(APP)

import userTemplate

CORS = CORS(APP, resources={r"/*": {"origins": "*"}})

USERLIST = []
TICLIST = ['', '', '', '', '', '', '', '', '']
XTURN = True
READY1 = False
READY2 = False

SOCKETIO = SocketIO(APP,
                    CORS_allowed_origins="*",
                    json=json,
                    manage_session=False)


@APP.route('/', defaults={"filename": "index.html"})
@APP.route('/<path:filename>')
def index(filename):
    """returns filename to the build"""
    return send_from_directory('./build', filename)


@SOCKETIO.on('connect')
def on_connect():
    """Display User Connecting"""
    print('User connected!')

@SOCKETIO.on('disconnect')
def on_disconnect():
    """Display User Disconnecting"""
    print('User disconnected!')


@SOCKETIO.on('chat')
def on_chat(data):
    """Forward User Chats"""
    SOCKETIO.emit('chat', data, broadcast=True, include_self=False)


@SOCKETIO.on('requestLeaderBoard')
def send_leader_board():
    """Send Leaderboard Data When Requested"""
    all_users = userTemplate.Template.query.all()
    user_lists = []
    rank_lists = []
    for person in all_users:
        user_lists.append(person.username)
        rank_lists.append(person.rank)
    SOCKETIO.emit('sentLeaderBoard', {'users': user_lists, 'rank': rank_lists})


@SOCKETIO.on('clickAttempt')
def on_click(data):
    """Update All Users Boards And Check For Win Condition"""
    global XTURN, TICLIST, READY1, READY2, DB
    success = False
    if ((XTURN) and READY1 and READY2 and (TICLIST[int(data.get('id'))] == '')
            and (data.get('username') == USERLIST[0])):
        success = True
        SOCKETIO.emit('clickSuccessX', data, broadcast=True, include_self=True)
        TICLIST[int(data.get('id'))] = 'X'
        XTURN = not XTURN
    elif ((not XTURN) and READY1 and READY2
          and (TICLIST[int(data.get('id'))] == '')
          and (data.get('username') == USERLIST[1])):
        success = True
        SOCKETIO.emit('clickSuccessO', data, broadcast=True, include_self=True)
        TICLIST[int(data.get('id'))] = 'O'
        XTURN = not XTURN
    else:
        SOCKETIO.emit('clickFailed', data, broadcast=True, include_self=True)

    if success:
        temp = 0
        if (TICLIST[0] != '' and TICLIST[0] == TICLIST[1]
                and TICLIST[1] == TICLIST[2]):
            temp = {'face': TICLIST[0], 'username': data.get('username')}

        elif (TICLIST[3] != '' and TICLIST[3] == TICLIST[4]
              and TICLIST[4] == TICLIST[5]):
            temp = {'face': TICLIST[3], 'username': data.get('username')}

        elif (TICLIST[6] != '' and TICLIST[6] == TICLIST[7]
              and TICLIST[7] == TICLIST[8]):
            temp = {'face': TICLIST[6], 'username': data.get('username')}

        elif (TICLIST[0] != '' and TICLIST[0] == TICLIST[3]
              and TICLIST[3] == TICLIST[6]):
            temp = {'face': TICLIST[0], 'username': data.get('username')}

        elif (TICLIST[1] != '' and TICLIST[1] == TICLIST[4]
              and TICLIST[4] == TICLIST[7]):
            temp = {'face': TICLIST[1], 'username': data.get('username')}

        elif (TICLIST[2] != '' and TICLIST[2] == TICLIST[5]
              and TICLIST[5] == TICLIST[8]):
            temp = {'face': TICLIST[2], 'username': data.get('username')}

        elif (TICLIST[0] != '' and TICLIST[0] == TICLIST[4]
              and TICLIST[4] == TICLIST[8]):
            temp = {'face': TICLIST[0], 'username': data.get('username')}

        elif (TICLIST[2] != '' and TICLIST[2] == TICLIST[4]
              and TICLIST[4] == TICLIST[6]):
            temp = {'face': TICLIST[2], 'username': data.get('username')}

        elif not '' in TICLIST:
            temp = {'face': '', 'username': data.get('username')}

        else:
            success = False

        if success:
            if temp['face'] != '':
                winner = DB.session.query(userTemplate.Template).filter_by(
                    username=temp['username']).first()
                winner.rank += 1
                DB.session.commit()
                if temp['username'] == USERLIST[1]:
                    loser = DB.session.query(userTemplate.Template).filter_by(
                        username=USERLIST[0]).first()
                    loser.rank -= 1
                    DB.session.commit()
                else:
                    loser = DB.session.query(userTemplate.Template).filter_by(
                        username=USERLIST[1]).first()
                    loser.rank -= 1
                    DB.session.commit()

            all_users = userTemplate.Template.query.all()
            user_lists = []
            rank_lists = []
            for person in all_users:
                user_lists.append(person.username)
                rank_lists.append(person.rank)
            SOCKETIO.emit('sentLeaderBoard', {
                'users': user_lists,
                'rank': rank_lists
            })
            SOCKETIO.emit('gameOver', temp, broadcast=True, include_self=True)
            temp = {'user0': USERLIST[0], 'user1': USERLIST[1]}
            SOCKETIO.emit('playAgainPrompt',
                          temp,
                          broadcast=True,
                          include_self=True)
            TICLIST = ['', '', '', '', '', '', '', '', '']
            READY1 = False
            READY2 = False
            XTURN = True


@SOCKETIO.on('playAgainAttempt')
def play_again_attempt(username):
    """Enable Game To Start When Player DecideS To Play Again"""
    global READY1, READY2
    if len(USERLIST) >= 2:
        if USERLIST[0] == username.get('username'):
            if not READY1:
                READY1 = True
            else:
                READY2 = True
            SOCKETIO.emit('playAgainSuccess',
                          username,
                          broadcast=False,
                          include_self=True)
        elif USERLIST[1] == username.get('username'):
            if not READY2:
                READY2 = True
            else:
                READY1 = True
            SOCKETIO.emit('playAgainSuccess',
                          username,
                          broadcast=False,
                          include_self=True)
        else:
            SOCKETIO.emit('playAgainFailed',
                          username,
                          broadcast=False,
                          include_self=True)
    else:
        SOCKETIO.emit('playAgainFailed',
                      username,
                      broadcast=False,
                      include_self=True)


@SOCKETIO.on('notAgainAttempt')
def not_again_attempt(username):
    """Enable Game To Start When Player Decides Not To Play Again"""
    global READY1, READY2
    if len(USERLIST) >= 2 and (USERLIST[0] == username.get('username')
                               or USERLIST[1] == username.get('username')):
        if USERLIST[0] == username.get('username'):
            if not READY1:
                READY1 = True
            else:
                READY2 = True
        elif USERLIST[1] == username.get('username'):
            if not READY2:
                READY2 = True
            else:
                READY1 = True
        USERLIST.remove(username.get('username'))
        USERLIST.append(username.get('username'))
        SOCKETIO.emit('notAgainSuccess',
                      username,
                      broadcast=False,
                      include_self=True)
        SOCKETIO.emit('USERLIST', USERLIST, broadcast=True, include_self=True)

    else:
        SOCKETIO.emit('notAgainFailed',
                      username,
                      broadcast=False,
                      include_self=True)


@SOCKETIO.on('loginAttempt')
def login_attempt(username):
    """Allow User To Login With A Unique Username"""
    global READY1, READY2
    if not username.get('username') in USERLIST:
        USERLIST.append(username.get('username'))
        all_users = userTemplate.Template.query.all()
        person_exist = False
        for person in all_users:
            if username.get('username') == person.username:
                person_exist = True
        if not person_exist:
            new_user = userTemplate.Template(username=username.get('username'),
                                             rank=100)
            DB.session.add(new_user)
            DB.session.commit()
            user_lists = []
            rank_lists = []
            for person in all_users:
                user_lists.append(person.username)
                rank_lists.append(person.rank)
            SOCKETIO.emit('sentLeaderBoard', {
                'users': user_lists,
                'rank': rank_lists
            })

        SOCKETIO.emit('loginSuccess',
                      username,
                      broadcast=False,
                      include_self=True)
        SOCKETIO.emit('USERLIST', USERLIST, broadcast=True, include_self=True)
        if len(USERLIST) == 1:
            READY1 = True
        elif len(USERLIST) == 2:
            READY2 = True

    else:
        SOCKETIO.emit('loginFailed',
                      username,
                      broadcast=False,
                      include_self=True)


@SOCKETIO.on('logoutAttempt')
def logout_attempt(username):
    """Allow User To Logout"""
    global READY1, READY2
    if username.get('username') in USERLIST:
        USERLIST.remove(username.get('username'))
        SOCKETIO.emit('logoutSuccess',
                      username,
                      broadcast=True,
                      include_self=True)
        SOCKETIO.emit('USERLIST', USERLIST, broadcast=True, include_self=True)
        if len(USERLIST) == 0:
            READY1 = False
        elif len(USERLIST) == 1:
            READY2 = False
    else:
        SOCKETIO.emit('logoutFailed',
                      username,
                      broadcast=False,
                      include_self=True)


if __name__ == "__main__":
    DB.create_all()
    SOCKETIO.run(
        APP,
        host=os.getenv('IP', '0.0.0.0'),
        port=8081 if os.getenv('C9_PORT') else int(os.getenv('PORT', 8081)),
    )
