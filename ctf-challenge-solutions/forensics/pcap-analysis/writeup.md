# Challenge Name: Sniffing the Network

## Challenge Details
- **Category:** Forensics
- **Difficulty:** Easy
- **Tools Used:** Wireshark, Python (Scapy)

## Vulnerability Explanation
Unencrypted network traffic (like HTTP, FTP, Telnet) transmits data in plain text, making it trivial for an intercepting party to capture credentials, files, and other sensitive information. This challenge required dissecting a PCAP file containing HTTP traffic.

## Step-by-Step Solution
1. **Reconnaissance:** Received `capture.pcap`. Opened it in Wireshark.
2. **Analysis:** Used the filter `http.request.method == "POST"` to find data being submitted by a user to a web server.
3. **Exploitation:** Found a POST request to `/login`. Upon examining the HTML Form URL Encoded data section of the packet payload, discovered a `user` and `password` parameter. 
4. **Post-Exploitation:** Realizing the CTF flag was passed as the password, it was simply extracted from the packet capture.

## Proof of Concept
```python
# The analyze.py script uses Scapy to automatically parse and dump POST payloads.
```

## Flag Format Example
`CTF{sn1ff1ng_pl4int3xt_cred5}`

## Defensive Recommendations
- Always encrypt sensitive network traffic. Do not use HTTP, FTP, or Telnet.
- Implement HTTPS (TLS 1.2 or higher) and secure protocols such as SFTP or SSH for administration.
