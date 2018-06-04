#!/usr/bin/env python3
# -*- mode: python-mode; python-indent-offset: 4 -*-
#
# Because my emacs session went nuts and started indenting 5

import configparser
import datetime
import json
import os
from urllib.parse import quote

import click
import frontmatter
import markdown
import requests


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
URL = "https://api.meetup.com/2/event"
GROUP = "hvopen"
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


def get_meetup_key():
    c = configparser.ConfigParser()
    c.read("config.ini")
    return c["default"].get("meetup_api_key")


def create_meetup(post):
    data = {
        "time": post.time,
        "key": get_meetup_key(),
        "sign": "true",
        "group_urlname": GROUP,
        "name": post.title,
        "description": post.description,
        "duration": post.duration
    }
    print(data)
    res = requests.post(URL, data=data)
    print("Status...")
    print(res.status_code)
    return json.loads(res.content.decode('utf-8'))


def update_meetup(post):
    url = URL + "/" + post.meetup_id
    data = {
        "time": post.time,
        "key": get_meetup_key(),
        "sign": "true",
        "group_urlname": GROUP,
        "name": post.title,
        "description": post.description,
        "duration": post.duration
    }
    print(data)
    res = requests.post(url, data=data)
    print("Status...")
    print(res.status_code)
    return json.loads(res.content.decode('utf-8'))


def all_events():
    events = []

    for root, dirs, files in os.walk("_events"):
        for f in files:
            if f.endswith(".md"):
                events.append(os.path.join(root, f))
    return events

def make_google_calendar_url(data):
    template = ("https://www.google.com/calendar/render?action=TEMPLATE&"
                "text=%(subject)s&"
                "dates=%(dtstart)s/%(dtend)s&"
                "details=%(desc)s&"
                "location=%(location)s&"
                "sprop=&sprop=name:")
    url = template % {
        "subject": quote(data['subject']),
        "desc": quote(data['description']),
        "location": quote(data['location']),
        "dtstart": data['dtstart'],
        "dtend": data['dtend']
    }
    return url


TEMPLATE = """
<table width="100%">
<tr>
<td align="center">
<table border="0" cellpadding="0" cellspacing="0" class="mcnButtonContentContainer" style="border-collapse: separate !important;border-radius: 3px;background-color: #2B
AADF;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">
                    <tbody>
                        <tr>
                            <td align="center" valign="middle" class="mcnButtonContent" style="font-family: Arial;font-size: 16px;padding: 15px;mso-line-height-rule: ex
actly;-ms-text-size-adjust: 100%%;-webkit-text-size-adjust: 100%%;">
                                <a class="mcnButton " title="RSVP on Meetup" href="{0}" target="_blank" style="font-weight: bold;letter-spacing: normal;line-height: 100
%;text-align: center;text-decoration: none;color: #FFFFFF;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;display: block;">RSVP
on Meetup</a>
                            </td>
                        </tr>
                    </tbody>
                </table>
</td>
<td align="center">
<table border="0" cellpadding="0" cellspacing="0" class="mcnButtonContentContainer" style="border-collapse: separate !important;border-radius: 3px;background-color: #2B
AADF;mso-table-lspace: 0pt;mso-table-rspace: 0pt;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">
                    <tbody>
                        <tr>
                            <td align="center" valign="middle" class="mcnButtonContent" style="font-family: Arial;font-size: 16px;padding: 15px;mso-line-height-rule: ex
actly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%;">
                                <a class="mcnButton " title="Add to Calendar" href="{1}"
style="font-weight: bold;letter-spacing: normal;line-height: 100%;text-align: center;text-decoration: none;color: #FFFFFF;mso-line-height-rule: exactly;-ms-text-size-ad
just: 100%;-webkit-text-size-adjust: 100%;display: block;">Add to Calendar</a>
                            </td>
                        </tr>
                    </tbody>
                </table>
</td>
</table>
"""  # noqa

def buttons(post):
    data = {
        "subject": post.title,
        "description": markdown.markdown(post._post.content),
        "dtstart": post.start.isoformat(),
        "dtend": post.end.isoformat(),
        "location": post.location.address
    }


    cal_url = make_google_calendar_url(data)

    print(TEMPLATE.format("https://meetup.com/hvopen/events/" + post.meetup_id, cal_url))



@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('event', type=click.Path(exists=True), required=True)
def main(event):
    """Sync events to meetup via the api

    The EVENT is the path to a file in the _events tree which will be
    synced to meetup.

    """
    post = Post(frontmatter.load(event))
    if post.meetup_id is None:
        resp = create_meetup(post)
        post.meetup_id = resp["id"]
        post.write(event)
    else:
        resp = update_meetup(post)
    # buttons(post)


if __name__ == '__main__':
    main()
