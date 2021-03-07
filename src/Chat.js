import { useState, useRef, useEffect } from 'react';
import { ListItem } from './ListItem.js';
import { SwitchDisplay, socket } from './App.js';
 // Connects to socket connection

export function Chat(props) {
  const [messages, setMessages] = useState([]); // State variable, list of messages
  const inputRef = useRef(null); // Reference to <input> element

  function onClickButton() {
    if (inputRef != null) {
      const message = inputRef.current.value;
      setMessages(prevMessages => [...prevMessages, "<you>: " + message]);
      socket.emit('chat', { username: props.username, message: message });
    }
  }

  useEffect(() => {
    socket.on('chat', (data) => {
      console.log('Chat event received!');
      console.log(data);
      setMessages(prevMessages => [...prevMessages, "<"+data.username+">: "+data.message]);
    });
    
    socket.on('loginSuccess', (data) => {
      console.log(data.username + ' has logged in.');
      setMessages(prevMessages => [...prevMessages, "User <"+data.username+"> has logged in."]);
    });
    
  socket.on('logoutSuccess', (data) => {
      console.log('Logout event received!');
      setMessages(prevMessages => [...prevMessages, "User <"+data.username+"> has logged out."]);
      if(props.username==data.username){
        SwitchDisplay(false, "null", true);
      }
    });
    
  socket.on('logoutFailed', (data) => {
      if(props.username==data.username){
        console.log('Logout event failed!');
      }
    });
    
  socket.on('print', (data) => {
      console.log('Chat event received!');
      console.log(data);
      setMessages(prevMessages => [...prevMessages, data]);
    });
    
  socket.on('gameOver', (data) => {
      console.log('Game Over event received!');
      if (data.face=='') {
        setMessages(prevMessages => [...prevMessages, "Draw!"]);
      }
      else {
        setMessages(prevMessages => [...prevMessages, "Player <"+ data.username + '> (' + data.face + ')' + " has Won!"]);
      }
    });
    
    
  }, []);

  return (
    <div id='chat' className='chat'>
      <h2>Chat Messages</h2>
      <ul className='scrollbox'>
        {messages.map((item, index) => <ListItem key={index} name={item} />)}
      </ul>
      Enter message here: <input ref={inputRef} type="text" />
      <button onClick={onClickButton}>Send</button>
    </div>
  );
}