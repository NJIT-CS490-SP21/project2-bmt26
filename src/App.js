import ReactDom from 'react-dom';
import { LoginPrompt } from './LoginPrompt.js';
import { Board } from './Board.js';
import { LogoutButton } from './LogoutButton.js';
import { PlayAgainButton } from './PlayAgainButton.js';
import { UserList } from './UserList.js';
import { Chat } from './Chat.js';
import { LeaderBoard } from './LeaderBoard.js'



export function App(props){
  const isLoggedIn = props.isLoggedIn;
  const username = props.username;
  const firstAttempt = props.firstAttempt;
  
  
  if (isLoggedIn===true) {
    return(
      <div className="App" id="display">
        <h1>Tic Tac Toe</h1>
        <div id='logged_in'>
          <ul>
            <li> 
              <UserList />
              <div id='user' className='chat'> Logged in as &lt;{username}&gt; <LogoutButton username={username} /> </div>
              <Chat username={username}/>
            </li>
            <li>
              <Board username={username}/>
              <div  id = 'play_again'> <PlayAgainButton username={username} firstAttempt={firstAttempt}/> </div>
            </li>
            <li> 
              <div  id = 'leaderboard' className='chat'> <LeaderBoard username={username} displayLeaderBoard={false}/> </div>
            </li>
          </ul>
        </div>
      </div>
      );
  }
  
  return(
    <div className="App" id="display">
      <LoginPrompt firstAttempt={firstAttempt}/>
    </div>
  );
      
}


export function SwitchDisplay(){
  ReactDom.render(
    <App isLoggedIn={arguments[0]} username={arguments[1]} firstAttempt={arguments[2]}/>,
    document.getElementById('display')
  )
}


export default App