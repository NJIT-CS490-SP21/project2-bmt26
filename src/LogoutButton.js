import { socket } from "./App.js";
import { React } from "react";
import PropTypes from "prop-types";

export function LogoutButton(props) {
  function onClickButton() {
    socket.emit("logoutAttempt", { username: props.username });
  }

  return <button onClick={onClickButton}>Logout</button>;
}

LogoutButton.propTypes = {
  username: PropTypes.node.isRequired,
};

export default LogoutButton;
