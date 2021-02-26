import './App.css';
import './Board.css';
import { UpdateDisplay } from './UpdateDisplay.js';


function App() {
  return (
    <div className="App" id="uiDiv">
      <UpdateDisplay isLoggedIn='false' username = 'null' firstAttempt = 'true'/>
    </div>
  );
}

export default App