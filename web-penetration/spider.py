import requests
import re
import urlparse

def extract_links_from(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content)

def crawl(url):
    href_links = extract_links_from(url)
    for link in href_links:
        parsed_link = urlparse.urljoin(url, link)

        if "#" in parsed_link:
            parsed_link = parsed_link.split('#')[0]

        if url in parsed_link and parsed_link not in target_links:
            target_links.append(parsed_link)
            print(parsed_link)
            crawl(parsed_link)


url = raw_input("Enter Target URL: \n")
protocol = raw_input("Is it using https? (y/n)")

if protocol is 'y' : protocol = 'https://'
if protocol is 'n' : protocol = 'http://'

target_url = "{}{}".format(protocol, url)
target_links = []

crawl(target_url)