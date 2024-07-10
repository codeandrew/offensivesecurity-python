import asyncio
import re
import urllib.parse as urlparse
from bs4 import BeautifulSoup
import random
import httpx

USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15; rv:70.0) Gecko/20100101 Firefox/70.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0",
]

class Scanner:
    def __init__(self, url, ignore_links) -> None:
        self.client = httpx.AsyncClient()
        self.set_user_agent()
        self.target_url = url
        self.target_links = []
        self.ignore_links = ignore_links
        self.reports = {
            "target": "",
            "directory": {"crawl": [], "traversal": []},
            "xss": [{"url": "", "form": "", "payload": ""}],
        }

    def set_user_agent(self):
        self.client.headers.update({"User-Agent": random.choice(USER_AGENTS)})

    async def extract_links_from(self, url):
        response = await self.client.get(url)
        return re.findall('(?:href=")(.*?)"', response.text)

    async def crawl(self, url=None):
        if url is None:
            url = self.target_url

        href_links = await self.extract_links_from(url)
        for link in href_links:
            parsed_link = urlparse.urljoin(url, link)

            if "#" in parsed_link:
                parsed_link = parsed_link.split("#")[0]

            if (
                self.target_url in parsed_link
                and parsed_link not in self.target_links
                and parsed_link not in self.ignore_links
            ):
                self.target_links.append(parsed_link)
                print(parsed_link)
                await self.crawl(parsed_link)

    async def extract_csrf_token(self, session, url):
        response = await session.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        token = soup.find("input", {"name": "user_token"})["value"]
        return token

    async def extract_forms(self, url):
        response = await self.client.get(url)
        parsed_html = BeautifulSoup(response.content, features="html.parser")
        return parsed_html.findAll("form")

    async def submit_form(self, form, value, url):
        action = form.get("action")
        method = form.get("method")
        post_url = urlparse.urljoin(url, action)

        input_list = form.findAll("input")
        post_data = {}
        for input in input_list:
            input_name = input.get("name")
            input_type = input.get("type")
            input_value = input.get("value")
            if input_type == "text":
                input_value = value

            post_data[input_name] = input_value
        if method == "post":
            return await self.client.post(post_url, data=post_data)
        return await self.client.get(post_url, params=post_data)

    async def run_scanner(self):
        tasks = []
        for link in self.target_links:
            tasks.append(self.scan_link(link))
        await asyncio.gather(*tasks)

    async def scan_link(self, link):
        forms = await self.extract_forms(link)

        for form in forms:
            print(f"[+] Testing form in: {link}")
            is_vulnerable_to_xss = await self.test_xss_in_form(form=form, url=link)
            if is_vulnerable_to_xss:
                print(f"\n[***] XSS Discovered in: {link}")
                print(form)
                print("===================================\n")

        if "=" in link:
            print(f"[+] Testing Link: {link}")
            is_vulnerable_to_xss = await self.test_xss_in_link(link)
            if is_vulnerable_to_xss:
                print(f"\n[***] XSS Discovered in: {link}")

    async def test_xss_in_link(self, url):
        xss_payload = "<sCript>alert('XSS PAYLOAD')</scriPt>"
        url = url.replace("=", f"={xss_payload}")
        response = await self.client.get(url=url)
        return xss_payload in response.text

    async def test_xss_in_form(self, form, url):
        xss_payload = "<sCript>alert('XSS PAYLOAD')</scriPt>"
        response = await self.submit_form(form=form, value=xss_payload, url=url)
        return xss_payload in response.text

async def dvwa_scan():
    target_url = "http://localhost"  # dvwa
    links_to_ignore = ["http://localhost/logout.php"]

    vuln_scanner = Scanner(url=target_url, ignore_links=links_to_ignore)
    login = f"{target_url}/login.php"
    token = await vuln_scanner.extract_csrf_token(vuln_scanner.client, url=login)
    dvwa_login = {
        "username": "admin",
        "password": "password",
        "Login": "submit",
        "user_token": token,
    }
    await vuln_scanner.client.post(login, data=dvwa_login)

    await vuln_scanner.crawl()
    await vuln_scanner.run_scanner()

async def example_scan():
    target_url = "http://192.168.254.109:2368/"
    links_to_ignore = ["http://localhost/logout.php"]
    vuln_scanner = Scanner(url=target_url, ignore_links=links_to_ignore)
    await vuln_scanner.crawl()
    await vuln_scanner.run_scanner()

if __name__ == "__main__":
    # asyncio.run(example_scan())
    asyncio.run(dvwa_scan())

"""
This is working but, the async scanner is still better, need to study more about async programming
"""