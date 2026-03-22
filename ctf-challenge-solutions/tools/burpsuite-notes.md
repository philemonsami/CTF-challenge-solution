# Burp Suite Cheatsheet

## Proxy
- **Intercept**: Allows pausing and modifying HTTP/HTTPS requests before they reach the server.
- **Match and Replace**: Automatically replace arbitrary strings in requests and responses (Proxy > Options).
- **Scope**: Define target scope to prevent logging out-of-scope traffic.

## Intruder
- **Sniper**: Targets a single payload position at a time. Ideal for simple fuzzing.
- **Battering Ram**: Places the same payload at multiple designated positions simultaneously.
- **Pitchfork**: Iterates through multiple payload sets simultaneously (e.g., Set 1 for username, Set 2 for password) on a 1-to-1 basis.
- **Cluster Bomb**: Tries all permutations of payloads. Useful for exhaustive credential brute-forcing.

## Repeater
- Manually edit request headers and body.
- Send the request multiple times and evaluate changes to the response.
- Follow redirects automatically or manually inside the Repeater window.

## Decoder
- Used to encode and decode various formats natively (URL, HTML, Base64, ASCII, Hex, Octal, Binary, GZIP).
- Smart decode: Attempts to automatically discern encoding type.

## Comparer
- Used to identify differences between two responses or requests.
- Input data can be loaded directly from Proxy or Repeater.
- Supports byte-level or word-level comparison.
