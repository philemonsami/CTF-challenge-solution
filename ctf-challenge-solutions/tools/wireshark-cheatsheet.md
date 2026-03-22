# Wireshark Cheatsheet

## General Usage
- **Interface**: Select the appropriate interface to capture traffic (e.g., eth0, wlan0).
- **Follow TCP Stream**: Right-click a packet -> Follow -> TCP Stream (reconstructs the entire application-level conversation).
- **Export Objects**: File -> Export Objects -> HTTP (Extract files from packet captures).

## Useful Display Filters
- `http` - Show only HTTP traffic.
- `http.request.method == "POST"` - Show only POST requests.
- `tcp.port == 80` - Filter by specific port.
- `ip.addr == 192.168.1.1` - Filter by specific IP (source or destination).
- `dns` - Show only DNS queries and responses.
- `frame contains "password"` - Search for a specific string inside packet payloads.
- `tls.handshake.type == 1` - Identify TLS Client Hello packets.

## Useful Shortcuts
- `Ctrl + E`: Start/Stop Capture.
- `Ctrl + F`: Search for packets.
- `Ctrl + R`: Reload capture file.
