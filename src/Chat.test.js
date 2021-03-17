/*eslint-disable*/
import { render, screen, fireEvent } from "@testing-library/react";
import Chat from "./Chat";

test("renders learn react link", () => {
  const result = render(<Chat username="user" />);

  const chat = document.getElementById("chat");
  const messagebox = document.getElementById("messagebox");
  const sendButtonElement = screen.getByText("Send");

  messagebox.innerHTML = "Test Sentence";
  fireEvent.click(sendButtonElement);

  //New Chat Message Added To Screen
  const text1 = screen.getByText("Test Sentence");
  expect(text1).toBeInTheDocument();

  messagebox.innerHTML = "a";
  fireEvent.click(sendButtonElement);

  //Previous and New Chats are present
  const text2 = screen.getByText("a");
  expect(text1).toBeInTheDocument();
  expect(text2).toBeInTheDocument();
});
