#!/usr/bin/env python3
# Challenge: Basic XOR License Crack
# Description: Reverses the XOR logic found in the decompiled crackme execution loop.
# Author: Educational Purpose

import argparse

def generate_key():
    """
    Reverses the hardcoded bytes found in the binary.
    In the binary, the logic showed the key was XORed with 0x5a
    and compared against the following target byte array.
    """
    # Hardcoded values extracted from Ghidra disassembly
    target_bytes = [0x19, 0x0e, 0x1c, 0x21, 0x28, 0x05, 0x31, 0x22, 0x23, 0x3d, 0x08, 0x19, 0x18, 0x34]
    
    # XOR Key extracted from assembly
    xor_key = 0x5a
    
    # Array to hold the successfully bypassed characters
    valid_license = []
    
    print("[*] Reversing licensing algorithm...")
    for byte in target_bytes:
        # A XOR B = C --> C XOR B = A
        orig_char = chr(byte ^ xor_key)
        valid_license.append(orig_char)
        
    final_key = ''.join(valid_license)
    print(f"[+] Valid License Key derived: {final_key}")
    
    return final_key

if __name__ == "__main__":
    generate_key()
