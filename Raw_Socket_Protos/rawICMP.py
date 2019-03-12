import struct
import socket
ICMP_HEAD_FMT="!BBHHH" #B is one byte; H is unsigned short (2 bytes) ! is for network (big-endian)
from .utils import calculate_checksum

class ICMPDatagram:
    """
    This class contains 8 bytes ICMP Datagram
    https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol#Control_messages

    <--------------32 bits-------------->
    --------------------------------------
    |  Type |  Code  |     Checksum      |
    --------------------------------------
    |   identifer    |  sequence #       | Each ping process has unique identifer and seq # is increasing within that
    --------------------------------------
    """

    def __init__(self, type=0, code=0, checksum=0, identifier=777, sequence=0):
        self.type = type
        self.code = code
        self.checksum = checksum # checksum of icmp
        self.identifier = identifier
        self.sequence = sequence

    def __repr__(self):
        return 'ICMPDatagram({},{},({},{}))'.format(self.type,self.code,self.checksum, self.data)

    def pack(self):
        icmp_header = struct.pack(ICMP_HEAD_FMT, self.type, self.code, self.checksum, self.identifier, self.sequence)
        self.checksum = calculate_checksum(icmp_header)
        icmp_header = struct.pack(ICMP_HEAD_FMT, self.type, self.code, self.checksum, self.identifier, self.sequence)
        return icmp_header


    def unpack(self, buffer):

        icmp_header_size = struct.calcsize(ICMP_HEAD_FMT)
        icmp_header_packed = buffer[:icmp_header_size]
        icmp_header = struct.unpack(ICMP_HEAD_FMT,icmp_header_packed)
        self.type = icmp_header[0]
        self.code = icmp_header[1]
        self.checksum = icmp_header[2]
        self.identifier = icmp_header[3]
        self.sequence = icmp_header[4]
        self.data = buffer[icmp_header_size:]
        #print ("buffer length  = " +str( len(buffer)) )
        #print ("data length  = " +str( len(self.data)) )



    #print ("icmp type = " + str(self.type))
        #print ("icmp code = " + str(self.code))
        #print ("icmp checksum = " + str(self.checksum))
        #print ("icmp identifier = " + str(self.identifier))
        #print ("icmp sequence = " + str(self.sequence))





