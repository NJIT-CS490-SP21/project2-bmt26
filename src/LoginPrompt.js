import io from 'socket.io-client';
import ReactDom from 'react-dom';
import {useState, useRef, useEffect} from 'react';
import { SwitchDisplay } from './UpdateDisplay.js';

const socket = io();
  
export function LoginPrompt(props) {
  const loginRef = useRef(null);
  const firstAttempt = props.firstAttempt;
  
  
  
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
        SwitchDisplay(true, username.username);
        //document.getElementById("loginDiv").remove();
      }
    });
    socket.on('loginFailed', (username) => {
      if(loginRef.current != null && loginRef.current.value==username.username){
        console.log('Login Failed: Username: <' + username.username + '> already taken.');
        loginFailedPrompt(false);
      }
    });
  }, []);
  
  
  if (firstAttempt==true) {
    return (
      <div id="loginDiv">
        <h1>Login to Enter or View Game</h1>
        Enter Username Here: <input ref={loginRef} type="text" />
        <button onClick={loginAttempt}>Login</button>
      </div>
    )
  }
  return (
    <div id="loginDiv"
    style={{
        left: '50%'
    }}
    >
      <h1>Login to Enter or View Game</h1>
      Enter Username Here: <input ref={loginRef} type="text" />
      <button onClick={loginAttempt}>Login</button>
      <br/>Username Taken. Try a Different One.
    </div>
  );
}


export function loginFailedPrompt(props){
    ReactDom.render(
    <LoginPrompt firstAttempt={props} />,
    document.getElementById('root')
    )
}


  
