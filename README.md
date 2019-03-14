# RawSocketsPython
Implementation of ICMP and UDP protocols (ping and traceroute )based on raw sockets python
This project defines all the headers from layer2 to layer4 -- no TCP though. I wanted to play with RawSockets in python so, I implemented the
ping Echo app on python Raw Sockets. Python Raw sockets provide options where you can supply your own headers ranging from etherent layer to any higher layer.

icmpEcho_layer4 implements ping while supplying only ICMP Header.<br/>
icmpEcho_layer3 implements ping while supplying only ICMP header and IPV4 Header.<br/>
icmpEcho_layer3 implements ping while supplying only ICMP header and IPV4 Header and Ethernet Header.<br/>

I have yet to write traceroute application. using all these header structures. 
But if anyone has any suggestion or if you find a bug, please let me know! 
Cheers 
