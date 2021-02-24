import ReactDom from 'react-dom';
import { Board, Login } from './UI.js';

export function UpdateDisplay(props){
  const isLoggedIn = props.isLoggedIn;
  if (isLoggedIn==true) {
    return(<Board />);
  }
  return(<Login />);
}


export function SwitchDisplay(props){
    ReactDom.render(
    <UpdateDisplay isLoggedIn={props} />,
    document.getElementById('root')
    )
}