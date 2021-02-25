import {useState, useRef, useEffect} from 'react';
import { Square } from './Square.js';

export function Board() {
  const [board, setBoard] = useState(['', '', '', '', '', '', '', '', '']);
  
  return (
    <div className="board" id="b" >
      <Square id="0" name={board[0]} />
      <Square id="1" name={board[1]} />
      <Square id="2" name={board[2]} />
      <Square id="3" name={board[3]} />
      <Square id="4" name={board[4]} />
      <Square id="5" name={board[5]} />
      <Square id="6" name={board[6]} />
      <Square id="7" name={board[7]} />
      <Square id="8" name={board[8]} />
    </div>
  )
};