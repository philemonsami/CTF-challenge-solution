#!/usr/bin/env python3
# Challenge: Frequency Analysis
# Description: Counts the frequency of characters in a given file.
# Author: Educational Purpose

import argparse
from collections import Counter

def analyze(file_path):
    """
    Reads a file and outputs a sorted list of character frequencies.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read().lower()
            
            # Count only alphabetic characters
            alphabet_only = [c for c in text if c.isalpha()]
            total_chars = len(alphabet_only)
            
            print(f"[*] Total Alphabetic Characters: {total_chars}")
            if total_chars == 0:
                print("[-] No alphabetic characters found.")
                return

            freqs = Counter(alphabet_only)
            
            print("\n[+] Character Frequencies (Sorted by most frequent):")
            for char, count in freqs.most_common():
                percentage = (count / total_chars) * 100
                print(f" '{char}' : {count:<5} | {percentage:.2f}%")
                
            print("\n[*] Standard English Frequency Order:")
            print(" e, t, a, o, i, n, s, h, r, d, l, c, u, m, w, f, g, y, p, b, v, k, j, x, q, z")
                
    except FileNotFoundError:
        print(f"[-] File not found: {file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Frequency Analysis Script")
    parser.add_argument("-f", "--file", required=True, help="Text file to analyze")
    args = parser.parse_args()
    
    analyze(args.file)
