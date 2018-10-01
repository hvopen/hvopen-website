import re

import markdown

LOCATION = """

Location:

{}
"""

LINK_STYLE="Margin:0;color:#1684B9;font-family:'Source Sans Pro',Helvetica,Arial,sans-serif;font-weight:400;line-height:1.3;margin:0;padding:0;text-align:left;text-decoration:none"  # noqa


def post_to_meetup(post):
    tags = ("h1", "h2", "h3", "h4")
    location = LOCATION.format(post.location.address)

    content = post.content + location

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
    if post.image:
        url = "https://hvopen.org{}".format(post.image)
        desc = """
<img src="{}" align="center" />
{}
""".format(url, desc)

    return desc


def post_to_mailchimp(post):
    html = markdown.markdown(post.content)
    html = re.sub("<a href", '<a style="%s" href"' % LINK_STYLE, html)
    return html
