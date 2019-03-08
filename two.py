#This file is similar to one except that instead of sending a udp packet, using sock_dgram
# I am gonna use socket_raw and construct udp header myself.

import socket
import struct
from Raw_Socket_Protos import rawUdp

remoteHost="www.dawn.com"
localHost = "192.168.50.59"
PORT = 33434

remoteHostIP = socket.gethostbyname(remoteHost)
print (remoteHostIP)
socketsender = socket.socket(family=socket.AF_INET, type=socket.SOCK_RAW, proto=socket.IPPROTO_UDP)
#socketsender.connect((remoteHostIP, PORT))
length = 8
checksum = 0
udp_header = struct.pack('!HHHH', PORT, PORT, length, checksum)
print (udp_header)
socketsender.setsockopt(socket.SOL_IP,socket.IP_TTL, 2)

socketsender.sendto(udp_header,(remoteHostIP,PORT) )
print ("sent")

receiversocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_RAW, proto=socket.IPPROTO_ICMP)
receiversocket.bind((localHost, PORT))
bytess, address = receiversocket.recvfrom(1024)
curr_name = address[0]
print ("--")
print (receiversocket.getsockopt(socket.SOL_IP, socket.IPPROTO_ICMP))
print (address)
print (curr_name)
print ("++")




