import React, {useState, useEffect} from 'react';
import io from 'socket.io-client';

const socket = io(); // Connects to socket connection

export function Square(props) {
    useEffect(() => {
    socket.on('click', (data) => {
        if (data.id==props.idops.id){
            console.log('Square #' + data.id + ' has changed to X by Opponent');
            document.getElementById(data.id).innerHTML = "X";
        }
    });
  }, []);
    
    return(
        
        <div id={props.id} className="box" onClick={() => clickDiv(props.id, props.name)}>{props.name}</div>
    )
}
        
function clickDiv(id, name) {
    console.log('Square #' + id + ' has changed to X by User');
    document.getElementById(id).innerHTML = "X";
    socket.emit('click', { id });
};