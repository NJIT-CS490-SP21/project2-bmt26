/*eslint-disable*/
import { render, screen, fireEvent } from "@testing-library/react";
import LoginPrompt from "./LoginPrompt";

test("renders learn react link", () => {
  const result = render(<LoginPrompt firstAttempt={true} />);

  const loginButtonElement = screen.getByText("Login");
  const usernameBox = document.getElementById("usernamebox");

  //Initial Check
  expect(loginButtonElement).toBeInTheDocument();

  //Login Button Does Not Disappears Whenever It is empty
  fireEvent.click(loginButtonElement);
  expect(loginButtonElement).toBeInTheDocument();

  //Username entered also does not cause login button to dissapear when clicked unless the server authorizes it
  usernameBox.innerHTML = "user";
  fireEvent.click(loginButtonElement);
  expect(loginButtonElement).toBeInTheDocument();
});
