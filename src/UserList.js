import io from 'socket.io-client';
import { useState, useEffect } from 'react';
import { ListItem } from './ListItem.js';

const socket = io(); // Connects to socket connection

export function UserList() {
  const [userList, setUserList] = useState([]); // State variable, list of users
  
  
  
  useEffect(() => {
    socket.on('userList', (data) => {
      console.log('User list received!');
      setUserList([]);
      for (const i in data) {
        if ( data[i]==data[0] ) {
          setUserList(prevMessages => [...prevMessages, "Player X: <"+ data[i] +">"]);
        }
        else if ( data[i]==data[1] ) {
          setUserList(prevMessages => [...prevMessages, "Player O: <"+ data[i] +">"]);
        }
        else {
          setUserList(prevMessages => [...prevMessages, "Spectator: <"+ data[i] +">"]);
        }
      }
    });
  }, []);
  
  
  return (
    <div className='chat'>
      <h2>User List</h2>
      <ul className='scrollbox'>
        {userList.map((item, index) => <ListItem key={index} name={item} />)}
      </ul>
    </div>
  );
}