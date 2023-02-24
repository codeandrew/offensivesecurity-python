import requests
import re
import urllib.parse as urlparse
from bs4 import BeautifulSoup

class Scanner:
    def __init__(self, url) -> None:
        self.target_url = url 
        self.target_links = []

    def extract_links_from(self, url):
        headers = {
            "Cookie": "PHPSESSID=oi7673bicmjlmcnthnrhvlmpt5; security=low; phpMyAdmin=6ff94ac6d748239b9c4f2a73c74f87ba; pma_lang=en; 5d89dac18813e15aa2f75788275e3588=bu0fc0d7ijh15nhknldosad50p"
        }
        response = requests.get(url, headers=headers)
        
        return re.findall('(?:href=")(.*?)"', response.text)

    def crawl(self, url=None):
        if url == None:
            url = self.target_url

        href_links = self.extract_links_from(url)
        for link in href_links:
            parsed_link = urlparse.urljoin(url, link)

            if "#" in parsed_link:
                parsed_link = parsed_link.split('#')[0]

            if self.target_url in parsed_link and parsed_link not in self.target_links:
                self.target_links.append(parsed_link)
                print(parsed_link)
                self.crawl(parsed_link)


def main(url):
    vuln_scanner = Scanner(url)
    vuln_scanner.crawl()


if __name__ == "__main__":
    target_url = "http://localhost"
    main(target_url)
