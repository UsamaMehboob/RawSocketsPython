import struct
ETH_HEAD_FMT="!BBBBBBBBBBBBH" #B is one byte; H is unsigned short (2 bytes) ! is for network (big-endian)

class EthernetFrame:
    """
    This class contains 14 bytes ethernet frame
    https://en.wikipedia.org/wiki/Ethernet_frame

    <--------------14 bytes (6+6+2)-------------->
    -------------------------------------------------------
    |  Destination Mac |  Source Mac  |     EtherType      |
    -------------------------------------------------------
    """

    def __init__(self, sourceMac='', destinationMac='', ethertype=0x0800, data=''):
        self.sourcemac=[0 for i in range(6)]
        self.destinationmac=[0 for i in range(6)]
        if sourceMac!='':
                sourcemacsplited = sourceMac.split(":")
                self.sourcemac[0] = int(sourcemacsplited[0],16)
                self.sourcemac[1] = int(sourcemacsplited[1],16)
                self.sourcemac[2] = int(sourcemacsplited[2],16)
                self.sourcemac[3] = int(sourcemacsplited[3],16)
                self.sourcemac[4] = int(sourcemacsplited[4],16)
                self.sourcemac[5] = int(sourcemacsplited[5],16)

        if destinationMac!='':
            destinationmacsplited = destinationMac.split(":")
            self.destinationmac[0] = int(destinationmacsplited[0],16)
            self.destinationmac[1] = int(destinationmacsplited[1],16)
            self.destinationmac[2] = int(destinationmacsplited[2],16)
            self.destinationmac[3] = int(destinationmacsplited[3],16)
            self.destinationmac[4] = int(destinationmacsplited[4],16)
            self.destinationmac[5] = int(destinationmacsplited[5],16)


        self.etherType = int(ethertype)

    def __repr__(self):
        return 'EthernetFrame ({},{},{},{})'.format(self.sourcemac,self.destinationmac,self.etherType, self.data)

    def pack(self):
        ethernet_header = struct.pack(ETH_HEAD_FMT, self.destinationmac[0], self.destinationmac[1], self.destinationmac[2],
                                      self.destinationmac[3],self.destinationmac[4],self.destinationmac[5],
                                      self.sourcemac[0],self.sourcemac[1],self.sourcemac[2],self.sourcemac[3],
                                      self.sourcemac[4],self.sourcemac[5],
                                      self.etherType
                                      )

        return ethernet_header


    def unpack(self, buffer):

        eth_header_size = struct.calcsize(ETH_HEAD_FMT)
        eth_header_packed = buffer[:eth_header_size]
        ethernet_header = struct.unpack(ETH_HEAD_FMT,eth_header_packed)
        self.destinationmac[0] = ethernet_header[0]
        self.destinationmac[1] = ethernet_header[1]
        self.destinationmac[2] = ethernet_header[2]
        self.destinationmac[3] = ethernet_header[3]
        self.destinationmac[4] = ethernet_header[4]
        self.destinationmac[5] = ethernet_header[5]
        self.sourcemac[0] = ethernet_header[6]
        self.sourcemac[1] = ethernet_header[7]
        self.sourcemac[2] = ethernet_header[8]
        self.sourcemac[3] = ethernet_header[9]
        self.sourcemac[4] = ethernet_header[10]
        self.sourcemac[5] = ethernet_header[11]
        self.etherType = ethernet_header[12]


        srcmacstr = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(self.sourcemac[0],self.sourcemac[1],self.sourcemac[2],
                                                                       self.sourcemac[3],self.sourcemac[4],self.sourcemac[5])
        dstmacstr = '{:02x}:{:02x}:{:02x}:{:02x}:{:02x}:{:02x}'.format(self.destinationmac[0],self.destinationmac[1],self.destinationmac[2],
                                                                       self.destinationmac[3],self.destinationmac[4],self.destinationmac[5])
        print (" srcmacstr :: == " + srcmacstr)
        print (" dstmacstr :: == " + dstmacstr)






