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
-1. Make sure you are working in the right branch. (git checkout milestone_1).
1. Add to Index (git add ".").
2. Make commits to local repository (git commit -m "Commit Message").
3. Push to remote repository branch on Github (git push origin milestone_1).


##
*Heroku
1. npm install-g heroku
2. heroku login -i
2. heroku create --buildpack heroku/python
3. heroku buildpacks:add --index 1 heroku/nodejs
4. git push heroku milestone\_1 (assuming you are downloading from milestone\_1 branch, else main will do fine)