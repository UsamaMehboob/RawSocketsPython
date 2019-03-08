import socket

remoteHost="www.dawn.com"
localHost = "192.168.50.59"
PORT = 33434

remoteHostIP = socket.gethostbyname(remoteHost)
print (remoteHost)
socketsender = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM, proto=socket.IPPROTO_IP)
#socketsender.connect((remoteHostIP, PORT))
socketsender.setsockopt(socket.SOL_IP,socket.IP_TTL, 3)
socketsender.sendto("".encode(),(remoteHostIP,PORT) )

receiversocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_RAW, proto=socket.IPPROTO_ICMP)
receiversocket.bind((localHost, PORT))
bytess, address = receiversocket.recvfrom(1024)
curr_name = address[0]
print ("--")
print (receiversocket.getsockopt(socket.SOL_IP, socket.IPPROTO_ICMP))
print (address)
print (curr_name)
print ("++")


#use them and see what is going on here: socketsender.getpeername() socketsender.getsockname() socket.socketype


#socketreceiver = socket.socket(family=socket.AF_INET, type=socket.SOCK_RAW)
#socketreceiver.bind((localHost,PORT))
#bytess, address = socketreceiver.recvfrom(1024)
#print (bytess, address)

