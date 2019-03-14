#This is an icmp protocol written using layer2  + , Means we will supply icmp header, ipv4 header
# and ethernet header. This is the lowest we can get using Raw sockets.
#s = socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ALL));

from Raw_Socket_Protos import rawICMP
from Raw_Socket_Protos import rawIPV4
from Raw_Socket_Protos import rawEthernet
import time
import socket
import struct

ICMP_ECHO_REQ = 8 #ping request
remoteHostIP = "8.8.8.8"
sourceip = "11.0.1.171"
#sourceip = "0.0.0.0"

socketsender = socket.socket(family=socket.AF_PACKET, type=socket.SOCK_RAW )
socketsender.bind(('eth0',0))
receiversocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_RAW, proto=socket.IPPROTO_ICMP)
receiversocket.bind((sourceip, 0))

sequencenumber = 0

while True:
    sequencenumber = sequencenumber + 1

    icmp_datagram = rawICMP.ICMPDatagram (type = ICMP_ECHO_REQ, sequence=sequencenumber)
    icmp_header = icmp_datagram.pack()
    ipv4_datagram = rawIPV4.IPV4Datagram(sourceip,remoteHostIP,ttl=227, protocol = socket.IPPROTO_ICMP, data = icmp_header)
    ipv4_header = ipv4_datagram.pack()
    ether_frame = rawEthernet.EthernetFrame(sourceMac ="12:38:32:be:4a:66",destinationMac="12:69:0a:60:d5:2e" )
    ether_header=ether_frame.pack()

    start = time.time()
    socketsender.send(ether_header+ipv4_header+icmp_header)
    bytess, address = receiversocket.recvfrom(1024)
    diff = int((time.time() - start ) * 1000 )
    ipv4_header = rawIPV4.IPV4Datagram()
    ipv4_header.unpack(bytess)
    icmp_header = rawICMP.ICMPDatagram()
    icmp_header.unpack(ipv4_header.data)
    if ( ipv4_header.source_ip == remoteHostIP ):
        print ( '{} bytes from {}: icmp_seq={} ttl={} time={} ms'.format(len(bytess),ipv4_header.source_ip,
                                                                         icmp_header.sequence, ipv4_header.ttl, diff))
    time.sleep(1)






