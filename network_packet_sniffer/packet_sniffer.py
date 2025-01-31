import socket
from scapy.all import sniff
from scapy.layers.inet import IP, UDP, TCP
from scapy.layers.l2 import Ether

def get_hostname(ip):
    """Attempts to resolve an IP address to a hostname."""
    try:
        #This will get the hostname linked with the ip
        hostname = socket.gethostbyaddr(ip)[0]
        return hostname
    except socket.herror:
        return "Unknown Host"


#This is the callback function which will process the packets
def callback(packet):
    src_ip = packet[IP].src
    dst_ip = packet[IP].dst
    src_host = get_hostname(src_ip)
    dst_host = get_hostname(dst_ip)

    #This will print a short summary of the packet
    print("\n=== Packet Captured===")
    print(f"Source: {src_ip} ({src_host}) -> Destination: {dst_ip} ({dst_host})")

    #Check for TCP layer
    if TCP in packet:
        print(f"TCP: {packet[TCP].sport} -> {packet[TCP].dport}, Flags: {packet[TCP].flags}")

    #Check for UDP layer
    elif UDP in packet:
        print(f"UDP: {packet[UDP].sport} -> {packet[UDP].dport}")

    #Check for Raw
    if packet.haslayer('Raw'):
        raw = packet['Raw'].load
        print(f"Raw Payload: {raw[:50]}")

    print("=======================")



#This will start the sniffing
def sniffing():
    #This will start sniffing on all the interfaces
    print("Sniffing on all network interfaces...")

    # This will capture 10 packets to process
    sniff(prn=callback, count=10)