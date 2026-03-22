# Python Snippets for CTFs

## HTTP Request Brute Force Template
```python
import requests

url = "http://target.local/login"
usernames = ["admin", "user"]
passwords = ["12345", "password", "admin"]

for user in usernames:
    for pwd in passwords:
        data = {"username": user, "password": pwd}
        r = requests.post(url, data=data)
        if "Incorrect password" not in r.text:
            print(f"[+] Found valid credentials - User: {user} | Pass: {pwd}")
            break
```

## Base64, Hex, URL Encoding/Decoding
```python
import base64
import urllib.parse
import binascii

plaintext = b"Secret String"

# Base64
b64_enc = base64.b64encode(plaintext)
b64_dec = base64.b64decode(b64_enc)

# Hex
hex_enc = binascii.hexlify(plaintext)
hex_dec = binascii.unhexlify(hex_enc)

# URL
url_enc = urllib.parse.quote("http://target.local/?id=1")
url_dec = urllib.parse.unquote(url_enc)
```

## RSA Modulus Extraction
```python
from Crypto.PublicKey import RSA

with open("public.pem", "r") as f:
    key = RSA.import_key(f.read())
    
print(f"Modulus (n): {key.n}")
print(f"Exponent (e): {key.e}")
```

## XOR Cracking Snippet
```python
def xor_strings(s1, s2):
    return bytes([a ^ b for a, b in zip(s1, s2)])

ciphertext = b"\x01\x02\x03"
key = b"KEY"
plaintext = xor_strings(ciphertext, key)
print(plaintext)
```

## Caesar Shift Brute Force Loop
```python
ciphertext = "Uif rvjdl cspxo gpy"

for shift in range(1, 26):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            plaintext += chr((ord(char) - start - shift) % 26 + start)
        else:
            plaintext += char
    print(f"Shift {shift}: {plaintext}")
```
