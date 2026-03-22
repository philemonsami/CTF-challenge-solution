
import argparse

def caesar_brute(ciphertext):
    """
    Tries all 25 possible shifts of a Caesar cipher.
    """
    for shift in range(1, 26):
        plaintext = ""
        for char in ciphertext:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
               
                plaintext += chr((ord(char) - start - shift) % 26 + start)
            else:
                plaintext += char
        print(f"[*] Shift {shift:02d}: {plaintext}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Caesar Cipher Solver")
    parser.add_argument("-c", "--ciphertext", required=True, help="Encrypted text to crack")
    args = parser.parse_args()
    
    
    print(f"[*] Testing ciphertext: {args.ciphertext}\n")
    caesar_brute(args.ciphertext)
