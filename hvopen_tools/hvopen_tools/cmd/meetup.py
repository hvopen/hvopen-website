#!/usr/bin/env python3

import configparser
import json
import os

import click
import frontmatter
import requests

from hvopen_tools.models import Post
from hvopen_tools.formatters import post_to_meetup

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
URL = "https://api.meetup.com/2/event"
GROUP = "hvopen"
VENUES = "https://api.meetup.com/{}/venues".format(GROUP)


def get_meetup_key():
    if os.environ.get("MEETUP_API"):
        return os.environ.get("MEETUP_API")

    c = configparser.ConfigParser()
    c.read("config.ini")
    return c["default"].get("meetup_api_key")


def meetup_post(url, post, venue_id=None):
    data = {
        "time": post.time,
        "key": get_meetup_key(),
        "sign": "true",
        "group_urlname": GROUP,
        "name": post.title,
        "description": post_to_meetup(post),
        "duration": post.duration
    }
    if venue_id:
        data["venue_id"] = venue_id
    print(data)
    res = requests.post(url, data=data)
    return json.loads(res.content.decode('utf-8'))


def create_meetup(post):
    return meetup_post(URL, post)


def update_meetup(post, venue_id):
    url = URL + "/" + post.meetup_id
    return meetup_post(url, post, venue_id)


def find_venue(name):
    data = {
        "key": get_meetup_key(),
        "sign": "true",
    }
    r = requests.get(VENUES, params=data)
    venues = json.loads(r.content)
    for v in venues:
        if v["name"].startswith(name):
            return v["id"]
    return None


def all_events():
    events = []

    for root, dirs, files in os.walk("_events"):
        for f in files:
            if f.endswith(".md"):
                events.append(os.path.join(root, f))
    return events


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('event', type=click.Path(exists=True), required=True)
def main(event):
    """Sync events to meetup via the api

    The EVENT is the path to a file in the _events tree which will be
    synced to meetup.

    """
    post = Post(frontmatter.load(event))
    if not post.meetup_id:
        resp = create_meetup(post)
        print(resp)
        post.meetup_id = resp["id"]
        post.write(event)
    else:
        venue_id = find_venue(post.location.title)
        resp = update_meetup(post, venue_id)


if __name__ == '__main__':
    main()
