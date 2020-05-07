#!/usr/bin/env python

import requests
from BeautifulSoup import BeautifulSoup

def request(url):
    try:
        return requests.get("http://{}".format(url))
    except requests.exceptions.ConnectionError:
        pass

target_url="10.0.2.15/mutillidae/index.php?page=dns-lookup.php"
response = request(target_url)

parsed_html = BeautifulSoup(response.content)
form_list = parsed_html.findAll("form")
print(form_list)