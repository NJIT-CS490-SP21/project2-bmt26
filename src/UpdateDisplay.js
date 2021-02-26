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
  const firstAttempt = props.firstAttempt;
  
  
  
  
  if (isLoggedIn==true) {
    return(
      <div>
        <Board username={username}/>
        Logged in as &lt;{username}&gt; <LogoutButton username={username}/>
        <div  id = 'text'>
          <PlayAgainButton username={username} firstAttempt={firstAttempt} id = {'text'}/>
        </div>
        <UserList />
        <Chat username={username}/>
      </div>
      );
  }
  return(<LoginPrompt firstAttempt={firstAttempt}/>);
}


export function SwitchDisplay(){
  ReactDom.render(
    <UpdateDisplay isLoggedIn={arguments[0]} username={arguments[1]} firstAttempt={arguments[2]}/>,
    document.getElementById('uiDiv')
  )
}


