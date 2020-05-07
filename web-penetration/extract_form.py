#!/usr/bin/env python

import requests
#from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup

def request(url):
    try:
        return requests.get("http://{}".format(url))
    except requests.exceptions.ConnectionError:
        pass

target_url="10.0.2.15/mutillidae/index.php?page=dns-lookup.php"
response = request(target_url)

parsed_html = BeautifulSoup(response.content, features='lxml')
form_list = parsed_html.findAll("form")

for form in form_list:
    action = form.get('action')
    print(action)
    method = form.get('method')
    print(method)

    input_list = form.findAll('input')
    print("\nInput names:")
    for input in input_list:
        input_name = input.get('name')
        print(input_name)