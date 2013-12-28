# -*- coding:utf-8 -*-
from collections import Counter
from datetime import datetime
import os
from urlparse import urlparse

from bottle import route, run, template
from bottle import static_file
from pymongo import MongoClient
from hn import HN


MONGO_URL = os.environ.get('MONGOHQ_URL')

if MONGO_URL: # for heroku
    client = MongoClient(MONGO_URL)
    db = client[urlparse(MONGO_URL).path[1:]]
else: # for local
    client = MongoClient('localhost', 27017)
    db = client["hackernews"]
top = db["top"]

def download(collection, stype, plimit):
    hn = HN()
    ids = []
    for s in hn.get_stories(story_type=stype, page_limit=plimit):
        story = {
            "_id":                  s.story_id,
            "rank":                 s.rank,
            "story_id":             s.story_id,
            "title":                s.title,
            "is_self":              s.is_self,
            "link":                 s.link,
            "domain":               s.domain,
            "points":               s.points,
            "submitter":            s.submitter,
            "submitter_profile":    s.submitter_profile,
            "published_time":       s.published_time,
            "num_comments":         s.num_comments,
            "comments_link":        s.comments_link,
            "time":                 datetime.now()
        }
        story_id = collection.save(story)
        ids.append(story_id)
    return len(ids)

@route('/', method='GET')
def get_titles():
    stories = top.find().sort("points", -1)
    return template('index', data=stories)

@route('/update_db', method='GET')
def update_db(count=0):
    # "" means "top". It's specification of the hn library.
    count = download(top, "", 7) 
    return template('<p>{{count}}</p>', count=count)

@route('/contents/<filename>')
def css(filename):
    return static_file(filename, root='./contents')

if MONGO_URL: # for heroku
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else: # for local
    run(host='localhost', port=8080, reloader=True)

