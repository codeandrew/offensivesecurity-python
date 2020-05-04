import requests
import re

def request(url):
    try:
        return requests.get("http://{}".format(url))
    except requests.exceptions.ConnectionError:
        pass

target_url = raw_input("Enter Target URL: \n")

response = request(target_url)

href_links = re.findall('(?:href=")(.*?)"', response.content)

print(href_links)