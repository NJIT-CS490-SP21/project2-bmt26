import React, {useState, useEffect} from 'react';
import io from 'socket.io-client';

const socket = io(); // Connects to socket connection

export function Square(props) {
    useEffect(() => {
    socket.on('click', (data) => {
      console.log('Click event received!');
      console.log(data.id);
      document.getElementById(data.id).innerHTML = "X";
    });
  }, []);
    
    return(
        
        <div id={props.id} class="box" onClick={() => clickDiv(props.id, props.name)}>{props.name}</div>
    )
}
        
function clickDiv(id, name) {
    console.log(id);
    document.getElementById(id).innerHTML = "X";
    socket.emit('click', { id });
}

