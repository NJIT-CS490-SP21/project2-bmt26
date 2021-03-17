/*eslint-disable*/
import { render, screen, fireEvent } from "@testing-library/react";
import LogoutButton from "./LogoutButton";

test("renders learn react link", () => {
  const result = render(<LogoutButton username="user" />);

  const logoutButtonElement = screen.getByText("Logout");

  expect(logoutButtonElement).toBeInTheDocument();

  //Logout Button Does Disappears Whenever It is Clicked and The Server Tells it to
  fireEvent.click(logoutButtonElement);
  expect(logoutButtonElement).toBeInTheDocument();
});
