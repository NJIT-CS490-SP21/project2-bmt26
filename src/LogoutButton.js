import io from 'socket.io-client';

const socket = io();

export function LogoutButton(props) {
    function onClickButton() {
        const username = props.username;
        socket.emit('logoutAttempt', { username: username });
    }
    
    return (
        <button onClick={onClickButton}>Logout</button>
    )
};