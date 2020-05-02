
import requests

url = "mail.google.com"
def request(url):
    try:
        get_response = requests.get("http://{}".format(url))
        print(get_response)
    except requests.exceptions.ConnectionError:
        pass


request(url)