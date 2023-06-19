import sys
from smb.SMBConnection import SMBConnection
from smb.smb_structs import OperationFailure

"""
# TESTED:
Python 3.10.6
pip3 install pysmb


# USAGE:
╰─$ python3 smb-check-access.py 10.10.10.10
[+] Share List
netlogon
profiles
print$
IPC$

[-] Access denied on share 10.10.97.132/netlogon -u Anonymous
[+] Access allowed on share 10.10.97.132/profiles -u Anonymous !
[-] Access denied on share 10.10.97.132/print$ -u Anonymous
[-] Access denied on share 10.10.97.132/IPC$ -u Anonymous
"""


class SMBEnum:
    def __init__(self, remote_ip):
        self.remote_name = ''
        self.remote_ip = remote_ip
        self.my_name = ''
        self.username = 'Anonymous'
        self.password = ''

    def connect(self):
        self.conn = SMBConnection(self.username, self.password, self.my_name, self.remote_name, use_ntlm_v2 = True)
        return self.conn.connect(self.remote_ip, 139)

    def get_share_list(self):
        shares = self.conn.listShares()
        print("[+] Share List")
        for share in shares:
            print(share.name)
        print()

    def test_anonymous_access(self):
        shares = self.conn.listShares()
        for share in shares:
            self.conn = SMBConnection(self.username, self.password, self.my_name, self.remote_name, use_ntlm_v2 = True)
            self.conn.connect(self.remote_ip, 139)
            try:
                # Attempt to list files in share
                file_list = self.conn.listPath(share.name, '/')
                print(f"[+] Access allowed on share {self.remote_ip}/{share.name} -u {self.username} !")
            except OperationFailure:
                print(f"[-] Access denied on share {self.remote_ip}/{share.name} -u {self.username}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 smb-check-access.py <remote_ip>")
        sys.exit(1)
    remote_ip = sys.argv[1]
    smb_enum = SMBEnum(remote_ip)
    if smb_enum.connect():
        smb_enum.get_share_list()
        smb_enum.test_anonymous_access()
    else:
        print("Connection failed.")
