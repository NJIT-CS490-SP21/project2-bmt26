import ReactDom from 'react-dom';
import { LoginPrompt } from './LoginPrompt.js';
import { Board } from './Board.js';
import { LogoutButton } from './LogoutButton.js';
import { PlayAgainButton } from './PlayAgainButton.js';
import { UserList } from './UserList.js';
import { Chat } from './Chat.js';
import './App.css';
import './Board.css';



export function UpdateDisplay(props){
  const isLoggedIn = props.isLoggedIn;
  const username = props.username;
  const firstAttempt = props.firstAttempt;
  
  
  if (isLoggedIn==true) {
    return(
      <div id='logged_in'>
        <ul>
          <li> <UserList /> </li>
          <li>
            <Board username={username}/>
            <div id='user'> Logged in as &lt;{username}&gt; <LogoutButton username={username}/> </div>
            <div  id = 'play_again'> <PlayAgainButton username={username} firstAttempt={firstAttempt}/> </div>
          </li>
          <li> <Chat username={username}/> </li>
        </ul>
      </div>
      );
  }
  
  return(<LoginPrompt firstAttempt={firstAttempt}/>);
}


export function SwitchDisplay(){
  ReactDom.render(
    <UpdateDisplay isLoggedIn={arguments[0]} username={arguments[1]} firstAttempt={arguments[2]}/>,
    document.getElementById('display')
  )
}


