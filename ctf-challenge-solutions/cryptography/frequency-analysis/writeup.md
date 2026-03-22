# Challenge Name: Missing Letters

## Challenge Details
- **Category:** Cryptography
- **Difficulty:** Easy
- **Tools Used:** Python, quipqiup

## Vulnerability Explanation
Substitution ciphers maintain the character frequency distribution of the original plaintext language. In English, the letter 'e' is the most common, followed by 't', 'a', 'o', 'i', 'n', etc. By analyzing the frequency of characters in a long enough ciphertext, an attacker can map the most frequent encrypted characters to the most frequent English letters to reconstruct the original message.

## Step-by-Step Solution
1. **Reconnaissance:** Received a long text document containing garbled text.
2. **Analysis:** The ciphertext did not use a simple Caesar shift (ROT13 failed). Because the text still had standard English punctuation and word boundary layouts, it was likely a monoalphabetic substitution cipher.
3. **Exploitation:** Wrote a Python script to calculate letter distributions. Mapped the most frequent letter 'q' to 'e'. Partially solved words like `thq` -> `the`, allowing further mapping of 't' and 'h'.
4. **Post-Exploitation:** Alternatively, feeding the cipher block into an automated solver like quipqiup handles dictionary pattern matching and solves the substitution cipher in seconds, revealing the flag hidden in paragraph 3.

## Proof of Concept
```python
# Run analyzer.py to show character counts and frequencies.
```

## Flag Format Example
`CTF{m0n0alpha_substract}`

## Defensive Recommendations
- Monoalphabetic ciphers are considered completely obsolete for securing data.
- Utilize modern standards such as AES for data at rest.
