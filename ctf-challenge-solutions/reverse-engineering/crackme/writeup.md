# Challenge Name: Simple license key

## Challenge Details
- **Category:** Reverse Engineering
- **Difficulty:** Medium
- **Tools Used:** Ghidra, Python, gdb

## Vulnerability Explanation
Software applications that handle arbitrary local license checks often contain internal logic determining if an inputted string is valid or not. By disassembling and decompiling the executable, an attacker can analyze the validation algorithm to reverse-engineer a valid license key or patch the executable to accept any input by swapping a conditional jump (`jz` to `jnz`).

## Step-by-Step Solution
1. **Reconnaissance:** Received an ELF executable `crackme1`. Executing it asks for a license key. Entering "test" returns "Access Denied."
2. **Analysis:** Opened `crackme1` in Ghidra. Navigated to the `main` function. Discovered a comparison loop that checks the characters of the inputted license key against a hardcoded array of XORed bytes.
3. **Exploitation:** Recreated the XOR logic in a Python script to decipher the hardcoded byte array. 
4. **Post-Exploitation:** Passed the reversed string into the executable: `./crackme1 $(python3 solver.py)`. The program outputted "Access Granted!" and the flag.

## Proof of Concept
```python
# The solver.py script performs the reverse XOR logic.
```

## Flag Format Example
`CTF{r3v3rs3_eng1n33r1n_fun}`

## Defensive Recommendations
- Implement obfuscation techniques to slow static analysis (though determined attackers will eventually bypass obfuscation).
- Relocate sensitive validation checks to a remote server environment rather than validating strictly on the client side.
