# -*- coding:utf-8 -*-
from collections import Counter
from datetime import datetime
import os
from urlparse import urlparse

from bottle import route, run, template
from bottle import static_file
from pymongo import MongoClient
from hn import HN

# Mongo DB Information
MONGO_URL = os.environ.get('MONGOHQ_URL')

if MONGO_URL: # for heroku
    client = MongoClient(MONGO_URL)
    db = client[urlparse(MONGO_URL).path[1:]]
else: # for local
    client = MongoClient('localhost', 27017)
    db = client["hackernews"]

collection = {
        "top":db["top"],
        "newest":db["newest"],
        "best":db["best"],
}

# Messages
MSG_ERR_PAGE_LIMIT = '<h2>Page Limit Error</h2><p>Between 1 and 10 are allowed.</p>'
MSG_ERR_COLLECTION_NAME = '<h2>Collection Name Error</h2><p>Only "top", "best" and "newest" collection are allowed.</p>'
MSG_ERR_INPUT_UPDATE = '<h2>Input</h2><p> Collection Name:{{collection_name}}, Page Limit:{{page_limit}} </p>'
MSG_ERR_INPUT_READ = '<h2>Input</h2><p> Collection Name:{{collection_name}}</p>'
MSG_INFO_STATUS = '<p> Get {{page_limit}} pages ({{count}} entries) from {{collection_name}}. </p>'

def download(collection, story_type, page_limit):
    hn = HN()
    ids = []
    for s in hn.get_stories(story_type=story_type, page_limit=page_limit):
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

# Routing
@route('/', method='GET')
def read_top():
    stories = collection["top"].find().sort("points", -1)
    return template('index', data=stories)

@route('/<collection_name>', method='GET')
def read(collection_name):
    if collection_name in ["top", "best", "newest"]:
        stories = collection[collection_name].find().sort("points", -1)
        return template('index', data=stories)
    else:
        return template(MSG_ERR_COLLECTION_NAME + MSG_ERR_INPUT_READ, 
                collection_name=collection_name)
    
    stories = collection["top"].find().sort("points", -1)
    return template('index', data=stories)

@route('/update/<collection_name>/<page_limit>', method='GET')
def update(collection_name, page_limit):
    page_limit = int(page_limit)
    if page_limit < 1 or page_limit > 10:
        return template(MSG_ERR_PAGE_LIMIT + MSG_ERR_INPUT_UPDATE, 
                collection_name=collection_name, page_limit=page_limit)

    if collection_name == "top":
        # "" means "top" by the specification of hn library.
        count = download(collection[collection_name], "", page_limit)
    elif collection_name in ["best", "newest"]:
        count = download(collection[collection_name], collection_name, page_limit)
    else:
        return template(MSG_ERR_COLLECTION_NAME + MSG_ERR_INPUT_UPDATE, 
                collection_name=collection_name, page_limit=page_limit)

    return template(MSG_INFO_STATUS, 
            collection_name=collection_name, page_limit=page_limit, count=count)

@route('/contents/<filename>')
def css(filename):
    return static_file(filename, root='./contents')

# Create HTTP Server
if MONGO_URL: # for heroku
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else: # for local
    run(host='localhost', port=8080, reloader=True)

