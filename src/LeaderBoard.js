import { useState, useEffect } from "react";
import { ListItem } from "./ListItem.js";
import ReactDom from "react-dom";
import { socket } from "./App.js";

export function LeaderBoard(props) {
  const displayLeaderBoard = props.displayLeaderBoard;
  const username = props.username;
  const [leaderBoard, setLeaderBoard] = useState([]); // State variable, list of users

  function showLeaderBoard() {
    ReloadLeaderBoard(username, true);
    socket.emit("requestLeaderBoard", { username: username });
  }

  function hideLeaderBoard() {
    ReloadLeaderBoard(username, false);
  }

  useEffect(() => {
    socket.on("sentLeaderBoard", (data) => {
      if (displayLeaderBoard) {
        console.log("Leaderboard received!");
        setLeaderBoard([]);
        for (var i in data["rank"]) {
          for (let j = i; j < data["rank"].length; j++) {
            if (data["rank"][i] < data["rank"][j]) {
              var temp1 = data["rank"][i];
              data["rank"][i] = data["rank"][j];
              data["rank"][j] = temp1;
              temp1 = data["users"][i];
              data["users"][i] = data["users"][j];
              data["users"][j] = temp1;
            }
          }
        }
        for (var i in data["rank"]) {
          if (data["users"][i] == username) {
            setLeaderBoard((prevMessages) => [
              ...prevMessages,
              data["users"][i] + ": " + data["rank"][i],
            ]);
            for (var j in data["rank"]) {
              if (i != j) {
                setLeaderBoard((prevMessages) => [
                  ...prevMessages,
                  data["users"][j] + ": " + data["rank"][j],
                ]);
              }
            }
            break;
          }
        }
      }
    });
  }, []);

  if (displayLeaderBoard) {
    return (
      <div>
        <h2>LeaderBoard</h2>
        <ul className="fullscrollbox">
          {leaderBoard.map((item, index) => (
            <ListItem key={index} name={item} />
          ))}
        </ul>
        <button onClick={hideLeaderBoard}>Hide LeaderBoard</button>
      </div>
    );
  }
  return <button onClick={showLeaderBoard}>Show LeaderBoard</button>;
}

function ReloadLeaderBoard() {
  ReactDom.render(
    <div id="leaderboard">
      <LeaderBoard username={arguments[0]} displayLeaderBoard={arguments[1]} />
    </div>,
    document.getElementById("leaderboard")
  );
}
