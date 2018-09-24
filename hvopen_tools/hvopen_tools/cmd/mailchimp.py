#!/usr/bin/env python3

import datetime
import json
import logging
import os

import click
import dateutil.tz
import frontmatter
import requests
from requests.auth import HTTPBasicAuth

from hvopen_tools.models import Post
from hvopen_tools.formatters import post_to_mailchimp
from hvopen_tools.mailchimp import mailchimp_button

_LOG = logging.getLogger(__name__)

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

API = "https://us14.api.mailchimp.com/3.0/"
API_KEY = os.environ.get("MC_API")
AUTH = HTTPBasicAuth('user', API_KEY)
LIST_ID = "6650a88ab6"
TEMPLATE_ID = 122801

DRY_RUN = False

UPCOMING_EVENT_TEMPLATE = """
<p>{date} - <a href="{url}">{name}</a></p>
"""


def mc_get(url):
    url = API + url
    return requests.get(url, auth=AUTH)


def mc_post(url, data):
    if DRY_RUN:
        return {"id": 1}

    URL = API + url
    resp = requests.post(URL, auth=AUTH, json=data)
    if resp:
        return json.loads(resp.content)
    else:
        _LOG.error("{} {}: {}".format(url, resp.status_code, resp.content))


def mc_put(url, data):
    if DRY_RUN:
        return {"id": 1}

    URL = API + url
    resp = requests.put(URL, auth=AUTH, json=data)
    if resp:
        return json.loads(resp.content)
    else:
        _LOG.error("{} {}: {}".format(url, resp.status_code, resp.content))


def create_campaign(name):
    data = {
        "type": "regular",
        "settings": {
            "title": name
        },
        "recipients": {
            "list_id": LIST_ID
        }
    }
    return mc_post("/campaigns", data)


def future_events():
    events = []

    for root, dirs, files in os.walk("_events"):
        for f in files:
            if f.endswith(".md"):
                fname = os.path.join(root, f)
                post = Post(frontmatter.load(fname))
                if post.start > datetime.datetime.now(
                        dateutil.tz.gettz("America/New York")):
                    events.append(post)
    return events

def events_to_list(events):
    html = ""
    for e in sorted(events, key=lambda x: x.start):
        html += UPCOMING_EVENT_TEMPLATE.format(
            name=e.title,
            url="https://meetup.com/hvopen/events/" + e.meetup_id,
            date=e.start.strftime("%b %e %l%P"))
    return html


def fill_template(c_id, post):
    url = "/campaigns/{}/content".format(c_id)

    upcoming_events = events_to_list(future_events())
    data = {
        "template": {
            "id": TEMPLATE_ID,
            "sections": {
                "$hvopen_prelim_callout_full_string_month": (
                    post.start.strftime("%B")),
                "$hvopen_talk_title": post.title,
                "$hvopen_talk_description": post_to_mailchimp(post),
                "$hvopen_cal_3char_month": post.start.strftime("%b"),
                "$hvopen_cal_date_e": post.start.day,
                "$hvopen_cal_date_time_lmp": post.start.strftime("%l%P"),
                "$hvopen_talk_image": post.image,
                "$hvopen_date_day_month_date_year": (
                    post.start.strftime("%a, %B %e, %Y")),
                # "$hvopen_time_span": "",
                # "$hvopen_location_full": "",
                "$hvopen_meetup_button_markup": mailchimp_button(
                    "RSVP on Meetup",
                    "https://www.meetup.com/hvopen/events/{}".format(post.meetup_id),
                    "#ffd503", "#000000"),
                "$hvopen_cal_button_markup": "",
                "$hvopenupcomingevents": upcoming_events

            }
        }
    }

    r = mc_put(url, data)
    if not r:
        _LOG.error("fill_template {}: {}".format(r.status_code, r.content))


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('event', type=click.Path(exists=True), required=True)
@click.option('--dry-run/--no-dry-run', default=False)
def main(event, dry_run=False):
    global DRY_RUN
    DRY_RUN=dry_run

    post = Post(frontmatter.load(event))
    if not post.meetup_id:
        return

    # TODO: find out if there is an existing campaign before stubbing it out.
    resp = create_campaign(post.title)
    if not resp:
        return 1
    fill_template(resp["id"], post)
    # print(json.dumps(resp, indent=4))


if __name__ == "__main__":
    main()
