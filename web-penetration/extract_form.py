#!/usr/bin/env python

import requests
#from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
import urlparse

def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

target_url="http://10.0.2.15/mutillidae/index.php?page=dns-lookup.php"
response = request(target_url)

parsed_html = BeautifulSoup(response.content, features='lxml')
form_list = parsed_html.findAll("form")

for form in form_list:
    action = form.get('action')
    post_url = urlparse.urljoin(target_url, action)
    method = form.get('method')

    input_list = form.findAll('input')
    post_data = {}
    for input in input_list:
        input_name = input.get('name')
        input_type = input.get('type')
        input_value = input.get('value')
        if input_type == 'text':
            input_value = 'test'

        post_data[input_name] = input_value
        
    print(post_data)
    result = requests.post(post_url, data=post_data)
    print(result.content)