import { useEffect } from 'react';
import ReactDom from 'react-dom';
import { socket } from './App.js';

export function PlayAgainButton(props) {
  const firstAttempt = props.firstAttempt;
  const username = props.username;
  
  useEffect(() => {
    
    socket.on('playAgainPrompt', (data) => {
      if (data.user0==username || data.user1==username) {
        SwitchButton(username, true);
      }
    });
    
    socket.on('playAgainSuccess', (data) => {
      if (data.username==username) {
        SwitchButton(username, false);
      }
    });
    
    socket.on('notAgainSuccess', (data) => {
      if (data.username==username) {
        SwitchButton(username, false);
      }
    });
    
    socket.on('playAgainFailed', (data) => {
      console.log("Attempt to Play Again Failed");
    });
    
    socket.on('notAgainFailed', (data) => {
      console.log("Attempt to Not Play Again Failed");
    });
    
  }, []);
  
  
  
  function playAgain() {
    socket.emit('playAgainAttempt', { username: username });
  }
  
  function notAgain() {
    socket.emit('notAgainAttempt', { username: username });
  }
  
  
  if(firstAttempt) {
    return (
      <div>
        <p>
          Play Again? 
          <button onClick={playAgain}>Yes</button>
          <button onClick={notAgain}>No</button>
        </p>
      </div>
    );
  }
  return(<br/>);
};


function SwitchButton(){
  ReactDom.render(
    <div  id = 'play_again'>
      <PlayAgainButton username={arguments[0]} firstAttempt={arguments[1]}/>
    </div>,
    document.getElementById('play_again')
  )
}