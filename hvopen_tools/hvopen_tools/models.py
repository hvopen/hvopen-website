import os
import datetime
import frontmatter


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
    def content(self):
        return self._post.content

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
