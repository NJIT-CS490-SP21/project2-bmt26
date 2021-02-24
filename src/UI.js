import {useState, useRef, useEffect} from 'react';
import { Square } from './Square.js';
import io from 'socket.io-client';
import { SwitchDisplay } from './UpdateDisplay.js';

const socket = io();
  
export function Login() {
  const loginRef = useRef(null);
  
  
  
  function loginAttempt() {
    if (loginRef != null && loginRef.current.value!="") {
      const username = loginRef.current.value;
      console.log('Login username ' + username + ' sent!');
      socket.emit('loginAttempt', { username: username });
    }
  }
  
  useEffect(() => {
    socket.on('loginSuccess', (username) => {
      console.log(username.username + ' has logged in.');
      if(loginRef.current != null && loginRef.current.value==username.username){
        console.log('Login successful! Username is ' + username.username);
        SwitchDisplay(true);
        //document.getElementById("loginDiv").remove();
      }
    });
  }, []);
  
  
  return (
    <div id="loginDiv">
      <h1>Login to Enter or View Game</h1>
      Enter Username Here: <input ref={loginRef} type="text" />
      <button onClick={loginAttempt}>Login</button>
    </div>
  );
}
    
    

  
  
export function Board() {
  const [board, setBoard] = useState(['', '', '', '', '', '', '', '', '']);
  
  return (
    <div className="board" id="b" >
      <Square id="0" name={board[0]} />
      <Square id="1" name={board[1]} />
      <Square id="2" name={board[2]} />
      <Square id="3" name={board[3]} />
      <Square id="4" name={board[4]} />
      <Square id="5" name={board[5]} />
      <Square id="6" name={board[6]} />
      <Square id="7" name={board[7]} />
      <Square id="8" name={board[8]} />
    </div>
  )
};