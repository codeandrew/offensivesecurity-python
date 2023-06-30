import socket
import smtplib

"""
version_tested: python 3.10.6

in main():
change 
rhosts =
username_list = 


# USAGE

╰─$ python3 smtp_enum-3.py
[+] target_ip = 10.10.129.130
[+] wordlist = username_list
[+] Banner:  220 polosmtp.home ESMTP Postfix (Ubuntu)

[+] User found: root
[+] User found: administrator
[+] User found: vagrant

"""

class SmtpScanner:
    def __init__(self, ip, port=25):
        self.ip = ip
        self.port = port
        self.smtp = None

    def connect(self):
        try:
            self.smtp = smtplib.SMTP(self.ip, self.port)
            return True
        except Exception as e:
            print(f"Could not connect: {e}")
            return False

    def get_banner(self):
        try:
            with socket.create_connection((self.ip, self.port), timeout=10) as sock:
                banner = sock.recv(1024).decode()
            return banner
        except Exception as e:
            print(f"Could not connect: {e}")
            return None

    def enumerate_users(self, user_file):
        if self.smtp is None:
            print("No connection.")
            return None

        users = []
        with open(user_file, 'r') as f:
            for line in f:
                username = line.strip()
                try:
                    code, msg = self.smtp.docmd("vrfy", username)
                    if code == 250 or code == 252:
                        print(f"[+] User found: {username}")
                        users.append(username)
                except Exception as e:
                    print(f"[+] Error verifying user {username}: {e}")
        return users
    

def main():
    rhosts =  '10.10.129.130'
    username_list = '/usr/share/wordlists/SecLists/Usernames/top-usernames-shortlist.txt'
    print(
        f"[+] target_ip = {rhosts}",
        f"\n[+] wordlist = username_list"
    )
    enumerator = SmtpScanner(rhosts)  
    if enumerator.connect():
        print("[+] Banner: ", enumerator.get_banner())
        enumerator.enumerate_users(username_list)  
    else:
        print("[-] Could not connect to the SMTP server.")

if __name__ == "__main__":
    main()
