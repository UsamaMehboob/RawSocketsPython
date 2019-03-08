import struct
import socket
ICMP_HEAD_FMT="!BBHI" #B is one byte; H is unsigned short (2 bytes) ! is for network (big-endian)

class ICMPDatagram:
    """
    This class contains 8 bytes ICMP Datagram
    https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol#Control_messages

    <--------------32 bits-------------->
    --------------------------------------
    |  Type |  Code  |     Checksum      |
    --------------------------------------
    |   Rest of the header               |
    --------------------------------------
    """

    def __init__(self, type=0, code=0, checksum=0, data=''):
        self.type = type
        self.code = code
        self.checksum = checksum # checksum of icmp
        self.data = data

    def __repr__(self):
        return 'ICMPDatagram({},{},({},{}))'.format(self.type,self.code,self.checksum, self.data)

    def pack(self):
        icmp_header = struct.pack(ICMP_HEAD_FMT, self.type, self.code, self.checksum, self.data)
        return icmp_header

    def unpack(self, buffer):
        icmp_header_size = struct.calcsize(ICMP_HEAD_FMT)
        icmp_header_packed = buffer[:icmp_header_size]
        icmp_header = struct.unpack(ICMP_HEAD_FMT,icmp_header_packed)
        self.type = icmp_header[0]
        self.code = icmp_header[1]
        self.checksum = icmp_header[2]
        self.data = buffer[icmp_header_size:]
        print ("icmp type = " + str(self.type))
        print ("icmp code = " + str(self.code))
        print ("icmp checksum = " + str(self.checksum))





