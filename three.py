#Here I am writing code on layer 2
#This file is similar to one except that instead of sending a udp packet, using sock_dgram
# I am gonna use socket_raw and construct udp header myself.

import socket
import struct
import sys
def ip2int(addr):
    return struct.unpack("!I", socket.inet_aton(addr))[0]

def calculate_checksum(source_string):
    #source_string = str(source_string)
    """
    A port of the functionality of in_cksum() from ping.c
    Ideally this would act on the string as a series of 16-bit ints (host
    packed), but this works.
    Network data is big-endian, hosts are typically little-endian
    """
    countTo = (int(len(source_string) / 2)) * 2
    sum = 0
    count = 0

    # Handle bytes in pairs (decoding as short ints)
    loByte = 0
    hiByte = 0
    while count < countTo:
        if (sys.byteorder == "little"):
            loByte = source_string[count]
            hiByte = source_string[count + 1]
        else:
            loByte = source_string[count + 1]
            hiByte = source_string[count]
        sum = sum + ((hiByte) * 256 + (loByte))
        count += 2

    # Handle last byte if applicable (odd-number of bytes)
    # Endianness should be irrelevant in this case
    if countTo < len(source_string): # Check for odd length
        loByte = source_string[len(source_string) - 1]
        sum += (loByte)

    sum &= 0xffffffff # Truncate sum to 32 bits (a variance from ping.c, which
    # uses signed ints, but overflow is unlikely in ping)

    sum = (sum >> 16) + (sum & 0xffff)	# Add high 16 bits to low 16 bits
    sum += (sum >> 16)					# Add carry from above (if any)
    answer = ~sum & 0xffff				# Invert and truncate to 16 bits
    answer = socket.htons(answer)

    return answer

remoteHost="www.dawn.com"
localHost = "192.168.50.59"
PORT = 33434

remoteHostIP = socket.gethostbyname(remoteHost)
print (remoteHostIP)
#socketsender.connect((remoteHostIP, PORT))
length = 8
checksum = 0
udp_header = struct.pack('!HHHH', PORT, PORT, length, checksum) #8 bytes; btw icmp is also 8 byte
#B is unsigned char(1), I is unsigned integer(4) and H is unsiged short (2)
version = 4
ihl = 5
version_ihl = (version << 4 )+ ihl #version is 4 and header length is 5 i.e 20 = 4*5 -- > 1 byte
dscp_ecn = 0 # 192 0xc0 --- > 1 byte # also called type of service.
total_length = 28 # -- > 2 bytes udp(8) + ipv4 (20)
identification = 50883 #-- > 2 bytes
flags_fragoffset = 0; # --> 2 bytes
ttl = 1 # -- > 1 byte
protocol = 17 # udp(17) icmp (1) -- > 1 byte
checksum = 0 # -- > 2 bytes
sourceip= socket.inet_aton(localHost) # -- > 4 bytes
destinationIp= socket.inet_aton(remoteHostIP) # -- > 4 bytes


ipv4_header = struct.pack('!BBHHHBBH4s4s', version_ihl, dscp_ecn, total_length, identification
                          ,flags_fragoffset,ttl,protocol,checksum,sourceip,destinationIp) #20bytes

checksum = calculate_checksum(ipv4_header)
print ("New checksum = "+ str(checksum))
ipv4_header = struct.pack('!BBHHHBBH4s4s', version_ihl, dscp_ecn, total_length, identification
                          ,flags_fragoffset,ttl,protocol,checksum,sourceip,destinationIp) #20bytes
print (udp_header)
print (ipv4_header)
print ("len == " + str (  len(ipv4_header)   )   )

socketsender = socket.socket(family=socket.AF_INET, type=socket.SOCK_RAW, proto=socket.IPPROTO_RAW)
#socketsender.setsockopt(socket.SOL_IP,socket.IP_TTL, 2)
socketsender.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
#socketsender.bind(('en0', 0))
socketsender.send(ipv4_header+udp_header)
#socketsender.sendto(ipv4_header+udp_header, (remoteHostIP,0) )

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




