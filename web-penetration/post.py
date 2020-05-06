#!/usr/env/python

import requests


target_url = ''
data_dict = {
    "username": "admin",
    "password": "password",
    "Login" : "submit"
}

response = requests.post(target_url, data_dict)
print(response.content)