
import requests

def request(url):
    try:
        return requests.get("http://{}".format(url))
    except requests.exceptions.ConnectionError:
        pass

target_url = raw_input("Enter Target URL: \n")

response = request(target_url)

print(response.content)