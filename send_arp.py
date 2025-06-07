from scapy.all import *

E = Ether(dst = '00:1D:9C:C8:BC:70', src = '00:1D:9C:C8:BD:30')  
A = ARP(op = 2, hwsrc = '00:1D:9C:C8:BD:30', psrc = '192.168.1.30', hwdst = '00:1D:9C:C8:BC:70', pdst = '192.168.1.70')  
pkt = E/A  
sendp(pkt)

E1 = Ether(dst = '00:1D:9C:C8:BD:30', src = '00:1D:9C:C8:BC:70')  
A1 = ARP(op = 2, hwsrc = '00:1D:9C:C8:BC:70', psrc = '192.168.1.70', hwdst = '00:1D:9C:C8:BD:30', pdst = '192.168.1.30')  
pkt1 = E1/A1 
sendp(pkt1)
    