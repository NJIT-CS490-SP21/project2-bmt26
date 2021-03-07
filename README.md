# Project1
## Imports
### This project utilizes Heroku for hosting the website, Socket for recieving and sending messags, React for updating the webpage and holding variables. Python imports include: os for retrieving port information, flask for backend handling

## Setup
### To setup this project you will need to:
1. Create a Heroku account
2. Download Heroku to your gitbash
3. In gitbash, sign into Heroku: `Heroku login -i` 
4. Create a Heroku app: `heroku create --buildpack heroku/python`
5. Add nodejs buildpack: `heroku buildpacks:add --index 1 heroku/nodejs`
6. Create a new database on your heroku: `heroku addons:create heroku-postgresql:hobby-dev`
7. Find the config vars of the new database `heroku config`
8. Put this value into DATABASE\_URL `export DATABASE_URL='result of heroku config goes here'`
9. Push to Heroku: `git push heroku main`
10. Start your database `sudo service postgresql start`
11. Open heroku using gitbash, and enter the page url in your web browser.

## Usage 
### When visiting the webpage, the user is prompted to submit a unqiue username to sign in. If the username is taken the user must type a different one. Once signed in, the users enter a queue, where the first and second users are allowed to click the tic tac toe squares and assign them X and O, respectively, in turn. Once there are three of the same letter in a row, or if the game ends in a draw, a dialog is sent to all users' chat logs alerting them the condition of the game ending, whether one user won, or the game was a draw. The top two players are then allowed to play again, or enter the queue from the back and let the next player in line play. All users are able to send messages to the chat log.

# Technical Issues
- In order to hide the Tic Tac Toe board I initially created propmted a change in style, but this lead to issues in styling, so I used ReactDom to load in the board depending on server messages
- The Chat history and User logs would default to blank when there was a game over. I had to make a reactdom specifically for the play again prompt, in the .jss file designated for the play again prompt.
- Creating a play again button had a lot of trouble, as I had to add in several server side variables that checked whether or not the players where ready before allowing any user to change the board. Additionally, I had to allow only the first two players to see the prompt, and prevent any other players from sending a message to the server thus, overriding the first and second players' choices.


# Known Issues
- Every message is broadcasted, so it uses up addtional server capabilities. I would investigate more on how to send to messages to specific users using socket.
- Chat history exists only for as long as the user has been connected, so old messages cannot be seen. I would add in a database to hold the chat log if I had more time.
- The css sizes are hardcoded, so they don't work well on very large or very small displays. I would add in a feature to base the css off of the browsers screen size.
- Users are not logged out when they disconnect, so closing the webpage or refreshing the browser without logging out first keeps the name in the queue, preventing users from logging into that username, or from playing if the user is the controller of X or O. If I had more time I would create a feature that automatically signs users out when disconnecting

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

# Flask and create-react-app

## Requirements
1. `npm install`
2. `pip install -r requirements.txt`

## Setup
1. Run `echo "DANGEROUSLY_DISABLE_HOST_CHECK=true" > .env.development.local` in the project directory

## Run Application
1. Run command in terminal (in your project directory): `python app.py`
2. Run command in another terminal, `cd` into the project directory, and run `npm run start`
3. Preview web page in browser '/'

## Deploy to Heroku
*Don't do the Heroku step for assignments, you only need to deploy for Project 2*
1. Create a Heroku app: `heroku create --buildpack heroku/python`
2. Add nodejs buildpack: `heroku buildpacks:add --index 1 heroku/nodejs`
3. Push to Heroku: `git push heroku main`

##
*Commits
-1. Make sure you are working in the right branch. (git checkout milestone_2).
1. Add to Index (git add ".").
2. Make commits to local repository (git commit -m "Commit Message").
3. Push to remote repository branch on Github (git push origin milestone_2).
