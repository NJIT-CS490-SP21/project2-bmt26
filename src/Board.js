import { React, useState } from "react";
import PropTypes from "prop-types";
import { Square } from "./Square.js";

export function Board(props) {
  const [board] = useState(["", "", "", "", "", "", "", "", ""]);

  return (
    <div className="board" id="b">
      <Square id="0" face={board[0]} username={props.username} />
      <Square id="1" face={board[1]} username={props.username} />
      <Square id="2" face={board[2]} username={props.username} />
      <Square id="3" face={board[3]} username={props.username} />
      <Square id="4" face={board[4]} username={props.username} />
      <Square id="5" face={board[5]} username={props.username} />
      <Square id="6" face={board[6]} username={props.username} />
      <Square id="7" face={board[7]} username={props.username} />
      <Square id="8" face={board[8]} username={props.username} />
    </div>
  );
}

Board.propTypes = {
  username: PropTypes.node.isRequired,
};
