import io from 'socket.io-client';

const socket = io();

export function PlayAgainButton(props) {
  function playAgain() {
    socket.emit('logoutAttempt', { username: props.username });
  }
  
  function notAgain() {
    socket.emit('logoutAttempt', { username: props.username });
  }
  
  
  
  return (
      <div>
        <p>Play Again?</p>
        <button onClick={playAgain}>Yes</button>
        <button onClick={notAgain}>No</button>
      </div>
    )
};