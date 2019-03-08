#in this file, I should try to send ip header as well alongwith udp header.
#in the file two_test, I successfully sent udp header but ip was constructed by kernel and
# I could see the packet got sent and captured by tcpdump with our specifications.
# Now i ma devleoping this file
#This file is similar to one except that instead of sending a udp packet, using sock_dgram
# I am gonna use socket_raw and construct udp header myself.

import socket
import struct
from rawUdp  import UDPDatagram
from rawICMP import ICMPDatagram
from rawIPV4 import IPV4Datagram



remoteHost="www.dawn.com"
localHost = "192.168.50.59"
PORT = 33434
remoteHostIP = socket.gethostbyname(remoteHost)
print (remoteHostIP)
socketsender = socket.socket(family=socket.AF_INET, type=socket.SOCK_RAW, proto=socket.IPPROTO_RAW)
#socketsender.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
udp_datagram = UDPDatagram(PORT,PORT)
udp_header =udp_datagram.pack()
ipv4_datagram = IPV4Datagram(localHost,remoteHostIP,ttl=2)
ipv4_header = ipv4_datagram.pack()
#socketsender.sendto(ipv4_header,(remoteHostIP,PORT) )
socketsender.sendto(ipv4_header+udp_header,(remoteHostIP,0) )
#socketsender.sendto(ipv4_header, (remoteHostIP,PORT) )

print ("sent")

receiversocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_RAW, proto=socket.IPPROTO_ICMP)
receiversocket.bind((localHost, PORT))
bytess, address = receiversocket.recvfrom(1024)
ipv4_header = IPV4Datagram("1.1.1.1","1.1.1.2")
ipv4_header.unpack(bytess)
icmp_header = ICMPDatagram()
icmp_header.unpack(ipv4_header.data)
curr_name = address[0]
print ("--")
print (receiversocket.getsockopt(socket.SOL_IP, socket.IPPROTO_ICMP))
print (address)
print (curr_name)
print ("++")





