import requests
import re
import urlparse

def extract_links_from(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content)

url = raw_input("Enter Target URL: \n")
target_url = "https://{}".format(url)

target_links = []

href_links = extract_links_from(target_url)

for link in href_links:
    parsed_link = urlparse.urljoin(target_url, link)
    target_links.append(target_url)
    print(parsed_link)