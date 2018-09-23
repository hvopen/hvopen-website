import markdown

LOCATION = """

Location:

{}
"""


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
    return markdown.markdown(post.content)
