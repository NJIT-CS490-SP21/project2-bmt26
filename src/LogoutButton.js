import io from 'socket.io-client';

const socket = io();

export function LogoutButton(props) {
    function onClickButton() {
        socket.emit('logoutAttempt', { username: props.username });
    }
    
    return (
        <button onClick={onClickButton}>Logout</button>
    )
};