import logo from './logo.svg';
import './App.css';
import './Board.css';
import { UpdateDisplay } from './UpdateDisplay.js';
import { Board, Login } from './UI.js';


function App() {
  return (
    <div className="App" id="uiDiv">
      <UpdateDisplay isLoggedIn='false'/>
    </div>
  );
}

export default App