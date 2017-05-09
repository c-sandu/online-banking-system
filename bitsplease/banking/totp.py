from hashlib import sha1
from time import time
from array import array

def totp(secret, moment):
    if moment == "prev":
        timestamp = int(time() / 30) - 1
    elif moment == "now":
        timestamp = int(time() / 30)
    elif moment == "next":
        timestamp = int(time() / 30) + 1

    first = str(secret) + str(timestamp)
    first = first.encode('utf-8')
    hash = sha1()
    hash.update(first)
    first = hash.hexdigest()
    
    second = str(secret) + first
    second = second.encode('utf-8')
    hash = sha1()
    hash.update(second)
    second = hash.digest()

    arr = array('B', second)
    bytes = arr[15:19]
    code = int.from_bytes(bytes, byteorder='big', signed=True)
    if code < 0:
        code = -code
        
    code = code % 1000000
    if len(str(code)) < 6:
        code = code * 10 ** (6 - len(str(code)))

    return str(code)
