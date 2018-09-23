#!/usr/bin/env python3

import datetime
import json
import os
from urllib.parse import quote


import click
import frontmatter
import markdown
import requests
from requests.auth import HTTPBasicAuth

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

API = "https://us14.api.mailchimp.com/3.0/"
API_KEY = os.environ.get("MC_API")
AUTH = HTTPBasicAuth('user', API_KEY)
LIST_ID = "6650a88ab6"
TEMPLATE_ID = 122801

LOCATION = """

Location:

{}
"""

ADDRESS = """
{title}
{addr}
{city}, {state} {zipcode}
""".replace("\n", "  \n")


class Location(object):
    def __init__(self, loc):
        self._loc = loc

    def _g(self, name):
        try:
            return self._loc[name]
        except KeyError:
            return ""

    @property
    def title(self):
        return self._g("title")

    @property
    def address(self):
        title = self._g("title")
        if self._g("subtitle"):
            title += "  \n" + self._g("subtitle")

        addr = self._g("address")
        if self._g("address1"):
            addr += "  \n" + self._g("address1")

        return ADDRESS.format(
            title=title,
            addr=addr,
            city=self._g("city"),
            state=self._g("state"),
            zipcode=self._g("zip")
        )


def find_location(name):
    for root, dirs, files in os.walk("_locations"):
        for f in files:
            location = frontmatter.load(os.path.join(root, f))
            print(location["title"])
            if location["title"] == name:
                return Location(location)
    raise Exception("No location found for {}".format(name))


class Post(object):

    def __init__(self, post):
        self._post = post
        self.start = datetime.datetime.strptime(
            post["dtstart"], "%Y-%m-%d %H:%M:%S %z")
        self.end = datetime.datetime.strptime(
            post["dtend"], "%Y-%m-%d %H:%M:%S %z")
        self.location = find_location(self._post["location"])

    @property
    def image(self):
        try:
            return self._post["image"]
        except KeyError:
            return ""

    @property
    def mailchimp_desc(self):
        return markdown.markdown(self._post.content)

    @property
    def description(self):
        tags = ("h1", "h2", "h3", "h4")
        location = LOCATION.format(self.location.address)

        content = self._post.content + location

        desc = markdown.markdown(content)
        for tag in tags:
            desc = desc.replace("<{}>".format(tag), "</p><p>")
            desc = desc.replace("</{}>".format(tag), ":</p>")

        # format out li
        desc = desc.replace("<li>", "* ")
        desc = desc.replace("</li>", "<br/>")
        # strip out ul
        desc = desc.replace("<ul>", "<p>")
        desc = desc.replace("</ul>", "</p>")
        if self.image:
            url = "https://hvopen.org{}".format(self.image)
            desc = """
<img src="{}" align="center" />
{}
""".format(url, desc)

        return desc

    @property
    def time(self):
        epoch = int(self.start.strftime('%s'))
        return epoch * 1000

    @property
    def duration(self):
        delta = self.end - self.start
        return delta.seconds * 1000

    @property
    def title(self):
        return self._post["title"]

    @property
    def meetup_id(self):
        try:
            meetup_id = self._post["meetup_id"]
        except KeyError:
            meetup_id = None
        return meetup_id

    @meetup_id.setter
    def meetup_id(self, value):
        self._post["meetup_id"] = str(value)

    def write(self, fname):
        with open(fname, "w") as f:
            f.write(frontmatter.dumps(self._post))


def mc_get(url):
    url = API + url
    return requests.get(url, auth=AUTH)


def mc_post(url, data):
    url = API + url
    return requests.post(url, auth=AUTH, json=data)


def mc_put(url, data):
    url = API + url
    return requests.put(url, auth=AUTH, json=data)


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
    r = mc_post("/campaigns", data)
    return json.loads(r.content)


def fill_template(c_id, post):
    url = "/campaigns/{}/content".format(c_id)

    print(post.mailchimp_desc)

    data = {
        "template": {
            "id": TEMPLATE_ID,
            "sections": {
                "$hvopen_prelim_callout_full_string_month": (
                    post.start.strftime("%B")),
                "$hvopen_talk_title": post.title,
                "$hvopen_talk_description": post.mailchimp_desc,
                "$hvopen_cal_3char_month": post.start.strftime("%b"),
                "$hvopen_cal_date_e": post.start.day,
                "$hvopen_cal_date_time_lmp": post.start.strftime("%l%P"),
                # "$hvopen_talk_image": "",
                "$hvopen_date_day_month_date_year": (
                    post.start.strftime("%a, %B %e, %Y")),
                # "$hvopen_time_span": "",
                # "$hvopen_location_full": "",
                "$hvopen_meetup_button_markup": "",
                "$hvopen_cal_button_markup": "",
                "$hvopenupcomingevents": "",

            }
        }
    }

    r = mc_put(url, data)
    print(r.status_code)
    print(r.content)


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('event', type=click.Path(exists=True), required=True)
def main(event):
    post = Post(frontmatter.load(event))
    if not post.meetup_id:
        return

    # TODO(sdague): find out if there is an existing campaign before stubbing it out.
    resp = create_campaign(post.title)
    fill_template(resp["id"], post)
    # print(json.dumps(resp, indent=4))


if __name__ == "__main__":
    main()
