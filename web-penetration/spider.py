import requests
import re

target_url = raw_input("Enter Target URL: \n")

def extract_links_from(url):
    response = requests.get("http://{}".format(url))
    return re.findall('(?:href=")(.*?)"', response.content)

href_links = extract_links_from(target_url)
print(href_links)