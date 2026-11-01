from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

def packet_callback(packet):
    """
    Callback function to process and display information about each captured packet.
    """
    if packet.haslayer(IP):
        ip_layer = packet.getlayer(IP)
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        
        proto_name = "OTHER"
        if packet.haslayer(TCP):
            proto_name = "TCP"
        elif packet.haslayer(UDP):
            proto_name = "UDP"
        elif packet.haslayer(ICMP):
            proto_name = "ICMP"

        print(f"\n[+] Packet Captured: {src_ip} ---> {dst_ip} | Protocol: {proto_name}")

        if packet.haslayer(TCP) or packet.haslayer(UDP):
            payload = packet.payload.payload
            if payload:
                print(f"    Payload: {bytes(payload)[:50]}...")
        elif packet.haslayer(ICMP):
            print("    Payload: ICMP Packet")

def main():
    print("=" * 60)
    print("Starting Network Sniffer... Press Ctrl+C to stop.")
    print("=" * 60)
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()