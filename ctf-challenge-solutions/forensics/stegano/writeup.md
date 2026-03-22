# Challenge Name: Hidden in Plain Sight

## Challenge Details
- **Category:** Forensics
- **Difficulty:** Medium
- **Tools Used:** Stegsolve, Python, Exiftool, zsteg

## Vulnerability Explanation
Steganography is the practice of concealing a file, message, image, or video within another file. A common technique is LSB (Least Significant Bit) manipulation in images (like PNGs or BMPs), where the final bit of the RGB values of pixels is altered to embed hidden data. The human eye cannot detect these minute changes.

## Step-by-Step Solution
1. **Reconnaissance:** Provided with `image.png`. The file opens fine as a standard picture.
2. **Analysis:** First ran `exiftool` and `strings` to verify there were no obvious appended payloads or metadata. 
3. **Exploitation:** Ran `zsteg image.png` which parses LSB steganography natively. It identified hidden ascii text in the `b1,r,lsb,xy` channel.
4. **Post-Exploitation:** Verified using a custom Python script that extracted the LSBs from the Red channel and grouped them into bytes, revealing the flag.

## Proof of Concept
```python
# The steg-solve.py script extracts LSB from a PNG image.
```

## Flag Format Example
`CTF{l3ast_s1gn1ficant_b1t}`

## Defensive Recommendations
- Steganography is mainly used to bypass DLP (Data Loss Prevention) mechanisms rather than securing data. 
- Implement aggressive anomaly detection on egress traffic and enforce image compression (which destroys LSB payloads) where strict file integrity is not required.
