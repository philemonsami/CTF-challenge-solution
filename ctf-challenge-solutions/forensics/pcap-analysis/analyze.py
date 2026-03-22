

import argparse

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import rdpcap, TCP, Raw

def analyze_pcap(pcap_file):
    """
    Parses a PCAP file and prints Outbound HTTP POST payloads.
    """
    try:
        print(f"[*] Reading {pcap_file} ...")
        packets = rdpcap(pcap_file)
        
        post_data_found = False
        
        for index, packet in enumerate(packets):
            if packet.haslayer(TCP) and packet.haslayer(Raw):
                payload = packet[Raw].load.decode(errors='ignore')
                
                
                if payload.startswith("POST"):
                    post_data_found = True
                    print(f"\n[+] POST Request found at packet {index + 1}:")
                    
                   
                    parts = payload.split("\r\n\r\n")
                    if len(parts) > 1:
                       
                        print("  Request:", parts[0].split("\n")[0])
                        
                        print("  Payload Data:", parts[1])
        
        if not post_data_found:
            print("[-] No HTTP POST data discovered in PCAP.")
            
    except Exception as e:
        print(f"[-] Error parsing PCAP: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract POST payloads from PCAPs")
    parser.add_argument("-f", "--file", required=True, help="Path to .pcap file")
    args = parser.parse_args()
    
    analyze_pcap(args.file)
