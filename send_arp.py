from scapy.all import *

E = Ether(dst = '00:1D:9C:C8:BC:46', src = '00:1D:9C:C8:BD:F2')  
A = ARP(op = 2, hwsrc = '00:1D:9C:C8:BD:F2', psrc = '192.168.1.30', hwdst = '00:1D:9C:C8:BC:46', pdst = '192.168.1.20')  
pkt = E/A  
sendp(pkt)

E1 = Ether(dst = '00:1D:9C:C8:BD:F2', src = '00:1D:9C:C8:BC:46')  
A1 = ARP(op = 2, hwsrc = '00:1D:9C:C8:BC:46', psrc = '192.168.1.20', hwdst = '00:1D:9C:C8:BD:F2', pdst = '192.168.1.30')  
pkt1 = E1/A1 
sendp(pkt1)
    