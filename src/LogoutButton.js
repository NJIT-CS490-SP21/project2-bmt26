import { socket } from "./App.js";

export function LogoutButton(props) {
  function onClickButton() {
    socket.emit("logoutAttempt", { username: props.username });
  }

  return <button onClick={onClickButton}>Logout</button>;
}
