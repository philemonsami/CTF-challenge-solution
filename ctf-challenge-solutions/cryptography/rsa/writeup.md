# Challenge Name: Small E RSA

## Challenge Details
- **Category:** Cryptography
- **Difficulty:** Medium
- **Tools Used:** Python, pycryptodome

## Vulnerability Explanation
The RSA implementation in this challenge uses a public exponent `e` of 3. If the message `m` is small enough that `m^e < n`, the modulus `n` does not wrap around. The encryption formula is `c = m^e mod n`. If there is no modulo wrap-around, `c` is simply `m^3`, and decryption becomes a straightforward process of calculating the cubic root of the ciphertext `c` over normal integers.

## Step-by-Step Solution
1. **Reconnaissance:** Received `public.pem`, `ciphertext.txt`. Extracted `n` and `e` from the public key, noticing that `e = 3`.
2. **Analysis:** Looked at the size of the ciphertext compared to `n` and determined that an unpadded, small message was encrypted. 
3. **Exploitation:** Wrote a script to take the integer cube root of `c`. Converted the numeric output back to bytes.
4. **Post-Exploitation:** The unpadded text successfully decoded into the readable flag.

## Proof of Concept
```python
# Run the enclosed decrypt.py to perform the attack.
```

## Flag Format Example
`CTF{sm4ll_e_p4dd1ng_f4il}`

## Defensive Recommendations
- Always use randomized padding schemes when working with RSA, such as OEAP (Optimal Asymmetric Encryption Padding). 
- Use standard values for `e`, such as 65537 (0x10001).
