import logo from './logo.svg';
import './App.css';
import './Board.css';
import { Board, Login } from './UI.js';


function App() {
  return (
    <div className="App" id="uiDiv">
      <Login />
      <Board />
    </div>
  );
}

export default App