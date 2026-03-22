# CTF Challenge Solutions Repository

## Overview
This repository contains a structured collection of Capture The Flag (CTF) challenge solutions, writeups, custom exploit scripts, and forensics/reverse engineering notes. It is designed to be a comprehensive reference guide for cybersecurity competitions and educational purposes.

## Categories Included
- **Web Exploitation**: Writeups for SQLi, XSS, CSRF, Authentication Bypass, and Directory Traversal.
- **Cryptography**: Solutions for Caesar cipher, RSA, XOR, and Frequency Analysis.
- **Forensics**: Notes on Memory analysis, PCAP analysis, Steganography, and Metadata extraction.
- **Reverse Engineering**: Solutions for crackmes, binary exploitation, and decompiler notes.
- **Tools**: Cheatsheets for Burp Suite, Wireshark, Metasploit, Python snippets, and custom wordlists.

## Folder Structure
```text
ctf-challenge-solutions/
├── web-exploitation/
├── cryptography/
├── forensics/
├── reverse-engineering/
├── tools/
├── templates/
├── README.md
└── requirements.txt
```

## Tools Used
- **Burp Suite**: Intercepting and modifying HTTP requests.
- **Wireshark**: Packet capture and network traffic analysis.
- **Metasploit**: Exploitation framework and payload generation.
- **Python**: Scripting language used for payloads, rapid prototyping, and automation.

## How to Use This Repo
1. **Browse Writeups**: Navigate to the respective category folder to read detailed writeups on specific vulnerabilities.
2. **Review Exploits**: Python proof of concepts are located alongside the writeups to demonstrate the attack in a local environment.
3. **Use Templates**: When attempting a new challenge, utilize the `templates/` directory to quickly spin up an exploit script or writeup structure.

## How to Run Scripts
1. Ensure you have Python 3 installed.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the target script (exercise caution and only run scripts against environments you have permission to test):
   ```bash
   python web-exploitation/sql-injection/exploit.py --url http://target.local/login
   ```

## How to Add New Writeups
1. Copy the `templates/full-writeup-template.md` (or `quick-writeup.md`).
2. Create a new directory under the appropriate category (e.g., `web-exploitation/new-vuln`).
3. Paste the template into a new file named `writeup.md` and fill in the details.
4. Add any accompanying exploit scripts using the `templates/exploit-template.py`.

## License
MIT License. This repository is for educational purposes only. Do not use these scripts or techniques against networks or applications you do not have explicit authorization to test.
