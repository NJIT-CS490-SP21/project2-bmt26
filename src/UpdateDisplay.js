import ReactDom from 'react-dom';
import { LoginPrompt } from './LoginPrompt.js';
import { Board } from './Board.js';
import { LogoutButton } from './LogoutButton.js';
import { PlayAgainButton } from './PlayAgainButton.js';
import { UserList } from './UserList.js';
import { Chat } from './Chat.js';
import { useEffect } from 'react';
import io from 'socket.io-client';

const socket = io();



export function UpdateDisplay(props){
  const isLoggedIn = props.isLoggedIn;
  const username = props.username;
  const restart = props.restart;
  
  useEffect(() => {
    socket.on('gameOver', (data) => {
      if (data.username==username) {
        Restart(isLoggedIn, username);
      }
    });
  }, []);
  
  
  if (isLoggedIn==true) {
    if (restart==true) {
      return(
        <div>
          <Board username={username}/>
          Logged in as &lt;{username}&gt; <LogoutButton username={username}/>
          <PlayAgainButton username={username}/>
          <UserList />
          <Chat username={username}/>
        </div>
      );
    }
    return(
      <div>
        <Board username={username}/>
        Logged in as &lt;{username}&gt; <LogoutButton username={username}/>
        <UserList />
        <Chat username={username}/>
      </div>
    );
  }
  return(<LoginPrompt firstAttempt={props}/>);
}

export function Restart(){
  ReactDom.render(
    <UpdateDisplay isLoggedIn={arguments[0]} username={arguments[1]} restart={true}/>,
    document.getElementById('root')
  )
}

export function SwitchDisplay(){
  ReactDom.render(
    <UpdateDisplay isLoggedIn={arguments[0]} username={arguments[1]} restart={false}/>,
    document.getElementById('root')
  )
}


