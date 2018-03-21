#!/usr/bin/env python3

import datetime
import json
import os
import re
from pathlib import Path

import frontmatter
import requests
import tomd


def to_dt(dt):
    return datetime.datetime.strptime(
        dt,
        "%Y-%m-%d %H:%M %z")


class Meeting(object):
    def __init__(self, data):
        self.title = data["title"]
        self._body = data["Body"]
        self.body = self._body
        self.url = data["Path"]
        self.dtstart = to_dt(data["dtstart"])
        self.dtend = to_dt(data["dtend"])
        self.location = data["Location"]
        self.presenter = data["Presenter"]
        if data["Presentation"] is not None:
            self.presentations = data["Presentation"].split(", ")
        self._clean()

    def _clean(self):
        def replace(matchobj):
            return "<" + matchobj.group(1) + ">"
        b = re.sub("<(h3|li|p)>\s+", replace, self._body)
        self.body = tomd.convert(b)

    @property
    def slug(self):
        return self.url.split("/")[-1]

    @property
    def path(self):
        return "_events/{}/{}-{}.md".format(
            self.dtstart.strftime("%Y"),
            self.dtstart.strftime("%Y-%m-%d"),
            self.slug
        )

    def dump(self):
        post = frontmatter.Post(self.body)
        post["title"] = self.title
        post["dtstart"] = self.dtstart.strftime("%Y-%m-%d %H:%M:%S %z")
        post["dtend"] = self.dtend.strftime("%Y-%m-%d %H:%M:%S %z")
        post["location"] = self.location
        post["mhvlug_url"] = self.url
        post["presenter"] = self.presenter
        post["type"] = "meeting"
        return frontmatter.dumps(post)

    def write(self):
        dname = os.path.dirname(self.path)
        if not os.path.exists(dname):
            os.mkdir(dname)
        with open(self.path, "w") as f:
            f.write(self.dump())


res = requests.get("https://mhvlug.org/export-all")
data = json.loads(res.content.decode('utf-8'))
for meeting in data["meetings"]:
    m = Meeting(meeting["meeting"])
    m.write()
