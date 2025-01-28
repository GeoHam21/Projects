from scapy.all import sniff

#This is the callback function which will process the packets
def callback(packet):
    #This will print a short summary of the packet
    print(packet.summary())


#This will display the packets to be viewed
def sniffing():
    #This will start sniffing on all the interfaces
    print("Sniffing on all network interfaces...")

    # This will capture 10 packets to process
    sniff(prn=callback, count=10)