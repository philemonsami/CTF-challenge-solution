#!/usr/bin/env python3
# Challenge: Basic LSB Stego Solver
# Description: Extracts Least Significant Bits from image channels.
# Author: Educational Purpose

import argparse
try:
    from PIL import Image
except ImportError:
    print("[-] Pillow library is not installed. Please install it (pip install Pillow).")
    exit()

def extract_lsb(image_path):
    """
    Extracts LSBs from a given image, converting bits to characters.
    """
    img = Image.open(image_path)
    pixels = list(img.getdata())
    
    extracted_bits = []
    
    for pixel in pixels:
        # Assuming RGB format, extract LSB of the Red channel (pixel[0])
        # Can scale to Green[1] and Blue[2] as needed
        extracted_bits.append(str(pixel[0] & 1))
        
    extracted_bits_str = "".join(extracted_bits)
    
    # Chunk bits by 8 to form bytes
    byte_chunks = [extracted_bits_str[i:i+8] for i in range(0, len(extracted_bits_str), 8)]
    
    extracted_message = ""
    for byte in byte_chunks:
        # Prevent partial trailing bits from erroring
        if len(byte) == 8:
            char = chr(int(byte, 2))
            extracted_message += char
            
            # Simple heuristic endpoint or just arbitrary cutoff
            if "</msg>" in extracted_message or len(extracted_message) > 500:
                break
                
    print("[+] Extracted string (first 500 chars):")
    # Only print printable ascii
    printable = ''.join(c for c in extracted_message if 32 <= ord(c) <= 126)
    print(printable)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LSB Steganography Extractor")
    parser.add_argument("-i", "--image", required=True, help="Image file to analyze")
    args = parser.parse_args()
    
    print(f"[*] Analyzing {args.image} for LSB...")
    extract_lsb(args.image)
