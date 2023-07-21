import aiohttp
import asyncio
import time
import json

url = "https://api.target.io/api/register"
number_of_requests = 500
concurrent_limit = 500  # adjust based on your system's capability

async def f(session, i):
    payload = {
        "email": f"demo_atk+{i}@email.com",
        "password": "s3cur3_th1s_sh1t"
    }

    headers = {
        'Content-Type': "application/json",
        'User-Agent': "PostmanRuntime/7.13.0",
        'Accept': "*/*",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    try:
        async with session.post(url, data=json.dumps(payload), headers=headers) as response:
            print(i, response.status, await response.text())
            return response.status

    except Exception as e:
        print(f"Request failed: {e}")
        return None

async def main():
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(number_of_requests):
            task = asyncio.ensure_future(f(session, i))
            tasks.append(task)
        responses = await asyncio.gather(*tasks)
        return responses

if __name__ == "__main__":
    start_time = time.time()
    print(f"[+] {number_of_requests} Requests")
    responses = asyncio.run(main())
    print("--- %s seconds ---" % (time.time() - start_time))

    success = len([r for r in responses if r and r // 100 == 2])
    server = len([r for r in responses if r and r // 100 == 5])
    error = len([r for r in responses if r and r // 100 == 4])

    print("success: ", success)
    print("server errors: ", server)
    print("client errors: ", error)
