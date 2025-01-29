from scapy.all import sniff
from scapy.layers.inet import IP, UDP, TCP
from scapy.layers.l2 import Ether

#This is the callback function which will process the packets
def callback(packet):
    #This will print a short summary of the packet
    print("\n=== Packet Captured===")

    #Check for ethernet layer
    if Ether in packet:
        print(f"Ethernet: {packet[Ether].src} -> {packet[Ether].dst}")

    #Check for IP layer
    if IP in packet:
        print(f"IP: {packet[IP].src} -> {packet[IP].dst}")

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