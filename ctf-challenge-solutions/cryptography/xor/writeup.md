# Challenge Name: Single-Byte XOR

## Challenge Details
- **Category:** Cryptography
- **Difficulty:** Easy
- **Tools Used:** Python, CyberChef

## Vulnerability Explanation
The XOR (Exclusive OR) logical operation is simple and reversible. When a plaintext is XORed against a single repeating byte, the encryption is extremely weak. A brute-force attack testing all possible 256 byte values (0x00 to 0xff) can quickly reveal the plaintext, provided a recognizable string or pattern (like a CTF flag format) is known to be in the plaintext.

## Step-by-Step Solution
1. **Reconnaissance:** Received a hex-encoded file `cypher.txt`. The hint says: "A single byte was the key to this transmission".
2. **Analysis:** Decoded the hex into raw bytes. The challenge is single-byte XOR.
3. **Exploitation:** Wrote a simple Python loop iterating from 0 to 255. XORed each byte of the ciphertext against the iterator value and checked if the resulting byte string contained "CTF{".
4. **Post-Exploitation:** The key was discovered to be `0x42` ('B'), revealing the concealed flag.

## Proof of Concept
```python
cipher_hex = "01160439050d11013d312102"
cipher_bytes = bytes.fromhex(cipher_hex)

for key in range(256):
    decrypted = bytes([b ^ key for b in cipher_bytes])
    if b"CTF{" in decrypted:
        print(f"Key: {hex(key)} - Plaintext: {decrypted}")
```

## Flag Format Example
`CTF{x0r_brut3f0rced}`

## Defensive Recommendations
- If using XOR for encryption, use a key that is the same length as the message and completely random (One-Time Pad - OTP). Never reuse the key.
- For practical security, use established cipher algorithms such as AES in an authenticated mode (e.g., GCM).
