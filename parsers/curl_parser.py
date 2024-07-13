import re

def parse_curl_command(file_path):
    with open(file_path, 'r') as file:
        curl_command = file.read().strip()

    # Extract URL
    url_match = re.search(r"curl '([^']*)'", curl_command)
    url = url_match.group(1) if url_match else None

    # Extract headers
    headers = dict(re.findall(r"-H '([^:]*): ([^']*)'", curl_command))

    # Extract data
    data_match = re.search(r"--data-raw '([^']*)'", curl_command)
    raw_data = data_match.group(1) if data_match else None
    data = dict(re.findall(r"([^=&]+)=([^&]*)", raw_data))

    return url, headers, data

if __name__ == "__main__":
    file_path = "curl.sh"
    url, headers, data = parse_curl_command(file_path)
    
    print("URL:", url)
    print("Headers:", headers)
    print("Data:", data)

"""
test references for this tool 
https://tryhackme.com/r/room/hackpark admin page

USAGE:
cat curl.sh
curl 'http://10.10.89.155/Account/login.aspx?ReturnURL=%2fadmin%2f' \
  -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8' \
  -H 'Accept-Language: en-US,en' \
  -H 'Cache-Control: max-age=0' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Origin: http://10.10.89.155' \
  -H 'Referer: http://10.10.89.155/Account/login.aspx?ReturnURL=/admin/' \
  -H 'Sec-GPC: 1' \
  -H 'Upgrade-Insecure-Requests: 1' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36' \
  --data-raw '__VIEWSTATE=nXHfYuqA534xpFQkk6W8SrUZNTcDpV%2FPQKezTUXeuJfrcMWTHBLtxWCdQc7VrGKzSfJt1Y44zTOgSTHQ0bgeVsJQZ0XPRkZ8YNtGe1eWYPaRGB%2FR%2F9CKOXZvWL%2Br5cJ3qR2vGpppxR5iP2Dwr8hlmf01Egxrg5RdXC38VFZoNU2aIQ7t&__EVENTVALIDATION=t8feE4JxAmSK7vpQVVd5kuBhs04HtAo5iDVznGukHJSGS55BtID8GP90SwWEblYqvJeaoMO0r78P8liuKDnPlSVeR%2FWbG5z8p1vXtxlBBzlrvlzSkJ1gHIKrfm6QHBgj6bDyZ3sy8fj%2BcLb6s0fA%2B2RRJbAOFGWYTh8oB1wcueJkutpM&ctl00%24MainContent%24LoginUser%24UserName=admin&ctl00%24MainContent%24LoginUser%24Password=FUZZ&ctl00%24MainContent%24LoginUser%24LoginButton=Log+in' \
  --insecure

╰─$ python3 curl_parser.py
URL: http://10.10.89.155/Account/login.aspx?ReturnURL=%2fadmin%2f
Headers: {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8', 'Accept-Language': 'en-US,en', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Origin': 'http://10.10.89.155', 'Referer': 'http://10.10.89.155/Account/login.aspx?ReturnURL=/admin/', 'Sec-GPC': '1', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}
Data: {'__VIEWSTATE': 'nXHfYuqA534xpFQkk6W8SrUZNTcDpV%2FPQKezTUXeuJfrcMWTHBLtxWCdQc7VrGKzSfJt1Y44zTOgSTHQ0bgeVsJQZ0XPRkZ8YNtGe1eWYPaRGB%2FR%2F9CKOXZvWL%2Br5cJ3qR2vGpppxR5iP2Dwr8hlmf01Egxrg5RdXC38VFZoNU2aIQ7t', '__EVENTVALIDATION': 't8feE4JxAmSK7vpQVVd5kuBhs04HtAo5iDVznGukHJSGS55BtID8GP90SwWEblYqvJeaoMO0r78P8liuKDnPlSVeR%2FWbG5z8p1vXtxlBBzlrvlzSkJ1gHIKrfm6QHBgj6bDyZ3sy8fj%2BcLb6s0fA%2B2RRJbAOFGWYTh8oB1wcueJkutpM', 'ctl00%24MainContent%24LoginUser%24UserName': 'admin', 'ctl00%24MainContent%24LoginUser%24Password': 'FUZZ', 'ctl00%24MainContent%24LoginUser%24LoginButton': 'Log+in'}


TODO: 
- try to urlparse if there's problem
"""