import ReactDom from 'react-dom';
import { LoginPrompt } from './LoginPrompt.js';
import { Board } from './Board.js';
import { LogoutButton } from './LogoutButton.js';
import { Chat } from './Chat.js';


export function UpdateDisplay(props){
  const isLoggedIn = props.isLoggedIn;
  const username = props.username;
  console.log(props);
  if (isLoggedIn==true) {
    return(
      <div>
        <Board />
        <LogoutButton username={username}/>
        <Chat />
      </div>
    );
  }
  return(<LoginPrompt firstAttempt={true}/>);
}


export function SwitchDisplay(){
    ReactDom.render(
    <UpdateDisplay isLoggedIn={arguments[0]} username={arguments[1]}/>,
    document.getElementById('root')
    )
}


