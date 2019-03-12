#This is an icmp protocol written using layer3 + , Means we will supply icmp header only and
#rest will be taken care by the kernel.

from Raw_Socket_Protos import rawICMP
from Raw_Socket_Protos import rawIPV4
import time
import socket

ICMP_ECHO_REQ = 8 #ping request
remoteHostIP = "8.8.8.8"
sourceip = "0.0.0.0"

socketsender = socket.socket(family=socket.AF_INET, type=socket.SOCK_RAW, proto=socket.IPPROTO_ICMP)
sequencenumber = 0

while True:
    sequencenumber = sequencenumber + 1
    icmpheaderdatagram = rawICMP.ICMPDatagram (type = ICMP_ECHO_REQ, sequence=sequencenumber)
    icmpheader = icmpheaderdatagram.pack()
    socketsender.sendto(icmpheader,(remoteHostIP,0) )
    time.sleep(1)
    bytess, address = socketsender.recvfrom(1024)
    ipv4_header = rawIPV4.IPV4Datagram()
    ipv4_header.unpack(bytess)
    icmp_header = rawICMP.ICMPDatagram()
    icmp_header.unpack(ipv4_header.data)
    if ( ipv4_header.source_ip == remoteHostIP ):
        print ( '{} bytes from {}: icmp_seq={} ttl={} time={}ms'.format(len(bytess),ipv4_header.source_ip,
                                                                     icmp_header.sequence, ipv4_header.ttl, 0))




