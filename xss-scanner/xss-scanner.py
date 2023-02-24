import requests
import urllib.parse as urlparse
from bs4 import BeautifulSoup

def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

target_url = "http://0.0.0.0/vulnerabilities/xss_r/"
response = request(target_url)

parsed_html = BeautifulSoup(response.content, features="html.parser")
forms_list = parsed_html.findAll("form")

for form in forms_list:
    action = form.get("action")
    method = form.get("method")

    post_url = urlparse.urljoin(target_url, action)
    print(
        f"URL: {post_url} : \n",
        "[+] Forms: \n"
        f"action: {action}",
        f"method: {method}"
    )

    payload = "XSS TEST"
    
    input_list = form.findAll("input")
    post_data = {}
    for input in input_list:
        input_name = input.get('name')
        input_type = input.get('type')
        input_value = input.get('value')
        if input_type == 'text':
            input_value = payload
        
        print("[+] Inputs")
        print(
            input_name
        )
        post_data[input_name] = input_value

    response = requests.post(post_url,data=post_data)

    """
    Form Extraction: Ok
    Post Payload: Not Sure
    """
    print(
        response.content
    )



