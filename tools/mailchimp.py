#!/usr/bin/env python3

import datetime
import json
import os
from urllib.parse import quote


# import click
# import frontmatter
# import markdown
import requests
from requests.auth import HTTPBasicAuth


API = "https://us14.api.mailchimp.com/3.0/"
API_KEY = os.environ.get("MC_API")
AUTH = HTTPBasicAuth('user', API_KEY)
LIST_ID = "6650a88ab6"
TEMPLATE_ID = 122801


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


def fill_template(c_id):
    url = "/campaigns/{}/content".format(c_id)

    data = {
        "template": {
            "id": TEMPLATE_ID,
            "sections": {
                "$hvopen_prelim_callout_full_string_month": "October",
                "$hvopen_talk_title": "Git 101",
                "$hvopen_talk_description": "blah!",
                "$hvopen_cal_3char_month": "Oct",
                "$hvopen_cal_date_e": "3",
                "$hvopen_cal_date_time_Imp": "6pm",
            }
        }
    }

    r = mc_put(url, data)
    print(r.status_code)
    print(r.content)


def main():
    resp = create_campaign("test 2")
    fill_template(resp["id"])
    print(json.dumps(resp, indent=4))


if __name__ == "__main__":
    main()
