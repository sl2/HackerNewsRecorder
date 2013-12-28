# Hacker News Recorder

A simple Hacker News Recorder & Reader for analytics.

![screen1](./hnrec.png)

## Environment

You can deploy this application following two environments.

1. local server, IaaS
2. heroku
	- MongoHQ is required

## Requirements

- [Python 2.7.x](http://www.python.org)
    - [Bottle](http://bottlepy.org/docs/dev/)
    - [PyMongo](https://pypi.python.org/pypi/pymongo/)
    - [karan / HackerNewsAPI](https://github.com/karan/HackerNewsAPI)
- [MongoDB](http://www.mongodb.org) or [MongoHQ](http://www.mongohq.com/home) (if you use heroku)

## Installation : Local server, IaaS

1. Download the repositry
         
        git clone https://github.com/sodesign/HackerNewsRecorder.git

2. Install required Python packages

        pip install bottle
        pip install pymongo
        pip install HackerNews==1.7.2

3. Start a MongoDB

4. Start the application

        python app.py

## Installation : heroku

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

    It is recommended to use crond.

2. Read it

        http://app_url

## ToDo

1. Add analytics
2. Improve reader
3. Improve database update method

## License

- MIT License

