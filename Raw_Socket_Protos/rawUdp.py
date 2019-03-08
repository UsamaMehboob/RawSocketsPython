import struct

UDP_HEAD_FMT="!HHHH" #H is unsigned short (2 bytes) ! is for network (big-endian)

class UDPDatagram:
    """
    This class contains 8 bytes UDP Datagram
    <--------------32 bits-------------->
    --------------------------------------
    |  Source Port  |   Destination Port |
    --------------------------------------
    |   length      |    checksum        |
    --------------------------------------
    """

    def __init__(self, sourcePort, destinationPort, length=8,data=''):
        self.sourcePort = sourcePort
        self.destinationPort = destinationPort
        self.length = length # this length is for header+data so minimum length is 8 and go to 65535-8(udp)-20(ip)
        self.checksum = 0    # we have option to use 0 for header cheksum of udp.

    def __repr__(self):
        return 'UDPDatagram({},{},({},{}))'.format(self.sourcePort,self.destinationPort,self.length,self.checksum)

    def pack(self):
        udp_header = struct.pack(UDP_HEAD_FMT, self.sourcePort, self.destinationPort, self.length, self.checksum)
        return udp_header

    def unpack(self, buffer):
        udp_header = struct.unpack(UDP_HEAD_FMT,buffer)
        self.sourcePort = udp_header[0]
        self.destinationPort = udp_header[1]
        self.length = udp_header[2]
        self.checksum = udp_header[3]
        return udp_header



