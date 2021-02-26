import './App.css';
import './Board.css';
import './UserList.css'
import { UpdateDisplay } from './UpdateDisplay.js';


function App() {
  return (
    <div className="App" id="display">
      <UpdateDisplay isLoggedIn='false' username = 'null' firstAttempt = 'true'/>
    </div>
  );
}

export default App