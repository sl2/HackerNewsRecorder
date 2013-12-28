# Hacker News Recorder

A simple Hacker News Recorder & Reader

## Environment

You can deploy this application following two environments.

1. local server, IaaS
2. heroku
	- MongoHQ is required

## Requirements

- Python 2.7.x
- MongoDB or MongoHQ (if you use heroku)

## Instllation : Local server, IaaS

1. Download the repositry
         
        git clone https://github.com/sodesign/HackerNewsRecorder.git

2. Install required Python packages

        pip install bottle
        pip install pymongo
        pip install HackerNews==1.7.2

3. Start a MongoDB

4. Start the application

        python app.py

## Instllation : heroku

1. Download the repositry
        
        git clone https://github.com/sodesign/HackerNewsRecorder.git

2. Deploy to heroku

        cd HackerNewsRecorder
        heroku apps:create [app name]
        git push heroku master

3. Add MongoHQ via heroku dashboard

4. Restart the application
        heroku restart --app [app name]


## Usage

1. Download new entries

        http://app_url/update_db

2. Read it

        http://app_url

## License

- MIT License

