import React, {useState, useEffect} from 'react';
import { socket } from './App.js';

export function Square(props) {
    useEffect(() => {
    socket.on('clickSuccessX', ( data ) => {
        if (data.id==props.id){
            console.log('Square #' + data.id + ' has changed to X by <' + data.username + '>');
            document.getElementById(data.id).innerHTML = "X";
        }
    });
    socket.on('clickSuccessO', ( data ) => {
        if (data.id==props.id){
            console.log('Square #' + data.id + ' has changed to O by <' + data.username + '>');
            document.getElementById(data.id).innerHTML = "O";
        }
    });
    socket.on('clickFailed', ( data ) => {
        if (data.username==props.username) {
            console.log('Click Failed');
            console.log(data);
        }
    });
    socket.on('gameOver', ( data ) => {
        console.log("Board Reset")
        document.getElementById(props.id).innerHTML = "";
    });
  }, []);
  
  
    function clickDiv(id, username) {
        console.log('Square #' + id + ' has been attempted to be changed by you (<' + username + '>)');
        socket.emit('clickAttempt',  {id: id, username: username} );
    }
    
    return(
        
        <div id={props.id} className="box" onClick={() => clickDiv(props.id, props.username)}>{props.face}</div>
    )
}
        


