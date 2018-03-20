#!/usr/bin/env python3

import configparser
import datetime
import json
import os

import frontmatter
import markdown
import requests

URL="https://api.meetup.com/2/event"

def get_meetup_key():
     c = configparser.ConfigParser()
     c.read("config.ini")
     return c["default"].get("meetup_api_key")

def dtstart_to_meetup(post):
    dt = datetime.datetime.strptime(post["dtstart"], "%Y-%m-%d %H:%M:%S %z")
    epoch = int(dt.strftime('%s'))
    return epoch * 1000

def create_meetup(post):
    data = {
        "time": dtstart_to_meetup(post),
        "key": get_meetup_key(),
        "sign": "true",
        "group_urlname": "Hudson-Valley-Open-Testing-Group",
        "name": post["title"],
        "description": markdown.markdown(post.content),
    }
    print(data)
    res = requests.post(URL, data=data)
    print("Status...")
    print(res.status_code)
    return json.loads(res.content.decode('utf-8'))


events = []

for root, dirs, files in os.walk("_events"):
    for f in files:
        if f.endswith(".md"):
            events.append(os.path.join(root, f))

for event in events:
    post = frontmatter.load(event)
    print(post['title'])
    try:
        meetup_id = post["meetup_id"]
    except KeyError:
        meetup_id = None

    if meetup_id is None:
        resp = create_meetup(post)
        post["meetup_id"] = resp["id"]
        with open(event, "w") as f:
            f.write(frontmatter.dumps(post))
