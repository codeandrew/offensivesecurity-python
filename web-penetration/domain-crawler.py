
import requests

url = "mail.google.com"
def request(url):
    try:
        return requests.get("http://{}".format(url))
    except requests.exceptions.ConnectionError:
        pass

domain_list = "subdomains.txt"
target_url = "google.com"

with open(domain_list, 'r') as wordlist_file:
    for line in wordlist_file:
        full_url = "{}.{}".format(line.strip(), target_url)
        response = request(full_url)
        if response:
            print("[+] Discovered subdomain --> {}".format(full_url))