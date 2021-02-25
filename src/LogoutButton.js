export function LogoutButton(props) {
    function onClickButton() {
        console.log("Test Logout Button");
  }
  
  return (
     <button onClick={onClickButton}>Logout</button>
  )
};