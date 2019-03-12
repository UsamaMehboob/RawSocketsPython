#This is an icmp protocol written using layer2  + , Means we will supply icmp header as well as ipv4 header
# Only ethernet header will be supplied by kernel.

from Raw_Socket_Protos import rawICMP
from Raw_Socket_Protos import rawIPV4
import time
import socket

ICMP_ECHO_REQ = 8 #ping request
remoteHostIP = "8.8.8.8"
#remoteHostIP = socket.gethostbyname("www.google.com")
sourceip = "0.0.0.0"

socketsender = socket.socket(family=socket.AF_INET, type=socket.SOCK_RAW, proto=socket.IPPROTO_RAW)
socketsender.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
sequencenumber = 0

while True:
    sequencenumber = sequencenumber + 1
    ipv4_datagram = rawIPV4.IPV4Datagram(sourceip,remoteHostIP,ttl=227, protocol = socket.IPPROTO_ICMP)
    ipv4_header = ipv4_datagram.pack()
    icmp_datagram = rawICMP.ICMPDatagram (type = ICMP_ECHO_REQ, sequence=sequencenumber)
    icmp_header = icmp_datagram.pack()

    start = time.time()
    socketsender.sendto(ipv4_header+icmp_header,(remoteHostIP,0) )
    # we have to use another socket as we wont be able to receive through IPPROTO_RAW
    receiversocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_RAW, proto=socket.IPPROTO_ICMP)
    receiversocket.bind((sourceip, 0))
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




