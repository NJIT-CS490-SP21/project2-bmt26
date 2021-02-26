import { useEffect } from 'react';
import io from 'socket.io-client';

const socket = io();

export function PlayAgainButton(props) {
  function playAgain() {
    socket.emit('playAgainAttempt', { username: props.username });
  }
  
  function notAgain() {
    socket.emit('notAgainAttempt', { username: props.username });
  }
  
  useEffect(() => {
    socket.on('playAgainFailed', (data) => {
      console.log("Attempt to Play Again Failed");
    });
    
    socket.on('notAgainFailed', (data) => {
      console.log("Attempt to Not Play Again Failed");
    });
  }, []);
  
  return (
      <div>
        <p>
          Play Again? 
          <button onClick={playAgain}>Yes</button>
          <button onClick={notAgain}>No</button>
        </p>
      </div>
    )
};