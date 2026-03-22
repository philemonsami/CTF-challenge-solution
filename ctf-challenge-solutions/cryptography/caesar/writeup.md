# Challenge Name: Veni Vidi Vici

## Challenge Details
- **Category:** Cryptography
- **Difficulty:** Easy
- **Tools Used:** Python, CyberChef

## Vulnerability Explanation
The Caesar cipher is a simple substitution cipher that replaces each letter in a text by a letter a fixed number of positions down the alphabet. Since there are only 25 possible shifts (keys) for the English alphabet, this encryption is completely vulnerable to brute-force attacks.

## Step-by-Step Solution
1. **Reconnaissance:** The challenge provides a ciphertext string that looks like scrambled letters, but preserves punctuation and word lengths (e.g., `synt{guvf_vf_n_pnrfne_pvcure}`).
2. **Analysis:** Noticed that "synt" might represent "flag". The difference between 's' (19) and 'f' (6) is 13, pointing to ROT13, a specific variant of Caesar.
3. **Exploitation:** Put the string into a Python brute-forcing script that loops through all 25 possible shift variations.
4. **Post-Exploitation:** Shift 13 rendered the successful plaintext.

## Proof of Concept
```python
# Run the enclosed solve.py script to brute-force all shifts.
```

## Flag Format Example
`CTF{this_is_a_caesar_cipher}`

## Defensive Recommendations
- Do not use Caesar cipher for securing sensitive data. It offers no serious cryptographic protection. Use modern cryptographic standards like AES.
