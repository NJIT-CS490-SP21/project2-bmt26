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
8. Put this value into DATABASE_URL `export DATABASE_URL='result of heroku config goes here'`
9. Push to Heroku: `git push heroku main`
10. Start your database `sudo service postgresql start`
11. Enable the Database using python `python`
    `from app import DB`
    `import userTemplate`
    `DB.create_all()`
    `DB.session.commit()`
12. Open heroku using gitbash, and enter the page url in your web browser.

## Usage

### When visiting the webpage, the user is prompted to submit a unqiue username to sign in. If the username is taken the user must type a different one. Once signed in, the users enter a queue, where the first and second users are allowed to click the tic tac toe squares and assign them X and O, respectively, in turn. Once there are three of the same letter in a row, or if the game ends in a draw, a dialog is sent to all users' chat logs alerting them the condition of the game ending, whether one user won, or the game was a draw. The top two players are then allowed to play again, or enter the queue from the back and let the next player in line play. All users are able to send messages to the chat log.

# Technical Issues

- Updating the rank of users in the database was difficult as I could not determine how to edit an old row. This was overcome by researching databases and determing I had to directly reference the database in the call.
- Ordering the users by rank was difficult as I didnt know how to reorder a database. I opted to simply sort them client side, as opposed to constantly updating the database.
- Reducing server lag was slightly troubling. It turned out to be an issue of declaring too many io sockets, and instead I declared one and exported it through every file that needed it.

# Known Issues

- Every message is broadcasted, so it uses up addtional server capabilities. I would investigate more on how to send to messages to specific users using socket.
- Chat history exists only for as long as the user has been connected, so old messages cannot be seen. I would add in a database to hold the chat log if I had more time.
- The css sizes are hardcoded, so they don't work well on very large or very small displays. I would add in a feature to base the css off of the browsers screen size.
- Users are not logged out when they disconnect, so closing the webpage or refreshing the browser without logging out first keeps the name in the queue, preventing users from logging into that username, or from playing if the user is the controller of X or O. If I had more time I would create a feature that automatically signs users out when disconnecting
