#!/usr/bin/env python3
# Challenge: Small E RSA Decryption
# Description: Uses integer cubic root to bypass RSA when e=3 and m^e < n.
# Author: Educational Purpose

import sys
import argparse
from Cryptodome.Util.number import long_to_bytes

def iroot(k, n):
    """
    Finds the integer k-th root of n.
    """
    u, s = n, n+1
    while u < s:
        s = u
        t = (k-1) * s + n // pow(s, k-1)
        u = t // k
    return s

def decrypt(c):
    """
    Decrypts ciphertext c by taking its cubic root.
    """
    m = iroot(3, c)
    if pow(m, 3) == c:
        print("[+] Exact cubic root found!")
        try:
            flag = long_to_bytes(m).decode("utf-8")
            print(f"[*] Decrypted Message: {flag}")
        except UnicodeDecodeError:
            print("[-] Decoded bytes are not valid UTF-8.")
            print(f"[*] Raw Bytes: {long_to_bytes(m)}")
    else:
        print("[-] C is not a perfect cube. Small e attack failed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="RSA e=3 Exploit")
    parser.add_argument("-c", "--ciphertext", type=int, required=True, help="Ciphertext as an integer")
    args = parser.parse_args()
    
    print("[*] Launching Small e Attack...")
    decrypt(args.ciphertext)
