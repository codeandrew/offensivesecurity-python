#!/usr/bin/env python

import requests

def request(url):
    try:
        return requests.get("http://{}".format(url))
    except requests.exceptions.ConnectionError:
        pass