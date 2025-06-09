"""
swat topology
"""

from mininet.topo import Topo
from mininet.node import RemoteController, OVSSwitch

from utils import IP, MAC, NETMASK


class SwatTopo(Topo):

    """SWaT 6 plcs + attacker + private dirs."""

    def build(self):

        # Tạo switch từ 0 -> 6
        # switch0 = self.addSwitch('s0', cls=OVSSwitch)
        # switch1 = self.addSwitch('s1', cls=OVSSwitch)
        # switch2 = self.addSwitch('s2', cls=OVSSwitch)
        # switch3 = self.addSwitch('s3', cls=OVSSwitch)
        # switch4 = self.addSwitch('s4', cls=OVSSwitch)
        # switch5 = self.addSwitch('s5', cls=OVSSwitch)
        # switch6 = self.addSwitch('s6', cls=OVSSwitch)

        switch0 = self.addSwitch('s0')
        switch1 = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')
        switch3 = self.addSwitch('s3')
        switch4 = self.addSwitch('s4')
        switch5 = self.addSwitch('s5')
        switch6 = self.addSwitch('s6')

        # Tạo link giữa s0 và s1 ->s6
        self.addLink(switch0,switch1)
        self.addLink(switch0,switch2)
        self.addLink(switch0,switch3)
        self.addLink(switch0,switch4)
        self.addLink(switch0,switch5)
        self.addLink(switch0,switch6)

        #Tạo host hmi
        hmi = self.addHost(
            'hmi',
            ip=IP['hmi'] + NETMASK,
            mac=MAC['hmi'])
        #Tạo link giữa hmi và s0
        self.addLink(hmi, switch0)

        #Tạo host plc1
        plc1 = self.addHost(
            'plc1',
            ip=IP['plc1'] + NETMASK,
            mac=MAC['plc1'])
        #Tạo link giữa plc1 và s1
        self.addLink(plc1, switch1)

        plc2 = self.addHost(
            'plc2',
            ip=IP['plc2'] + NETMASK,
            mac=MAC['plc2'])
        self.addLink(plc2, switch1)

        plc3 = self.addHost(
            'plc3',
            ip=IP['plc3'] + NETMASK,
            mac=MAC['plc3'])
        self.addLink(plc3, switch1)

        plc4 = self.addHost(
            'plc4',
            ip=IP['plc4'] + NETMASK,
            mac=MAC['plc4'])
        self.addLink(plc4, switch1)

        plc5 = self.addHost(
            'plc5',
            ip=IP['plc5'] + NETMASK,
            mac=MAC['plc5'])
        self.addLink(plc5, switch1)

        plc6 = self.addHost(
            'plc6',
            ip=IP['plc6'] + NETMASK,
            mac=MAC['plc6'])
        self.addLink(plc6, switch1)

        #Tạo host plc1
        plc7 = self.addHost(
            'plc7',
            ip=IP['plc7'] + NETMASK,
            mac=MAC['plc7'])
        #Tạo link giữa plc1 và s1
        self.addLink(plc7, switch2)

        plc8 = self.addHost(
            'plc8',
            ip=IP['plc8'] + NETMASK,
            mac=MAC['plc8'])
        self.addLink(plc8, switch2)

        plc9 = self.addHost(
            'plc9',
            ip=IP['plc9'] + NETMASK,
            mac=MAC['plc9'])
        self.addLink(plc9, switch1)

        plc10 = self.addHost(
            'plc10',
            ip=IP['plc10'] + NETMASK,
            mac=MAC['plc10'])
        self.addLink(plc10, switch2)

        plc11 = self.addHost(
            'plc11',
            ip=IP['plc11'] + NETMASK,
            mac=MAC['plc11'])
        self.addLink(plc11, switch2)

        plc12 = self.addHost(
            'plc12',
            ip=IP['plc12'] + NETMASK,
            mac=MAC['plc12'])
        self.addLink(plc12, switch2)

        #Tạo host plc1
        plc13 = self.addHost(
            'plc13',
            ip=IP['plc13'] + NETMASK,
            mac=MAC['plc13'])
        #Tạo link giữa plc1 và s1
        self.addLink(plc13, switch3)

        plc14 = self.addHost(
            'plc14',
            ip=IP['plc14'] + NETMASK,
            mac=MAC['plc14'])
        self.addLink(plc14, switch3)

        plc15 = self.addHost(
            'plc15',
            ip=IP['plc15'] + NETMASK,
            mac=MAC['plc15'])
        self.addLink(plc15, switch3)

        plc16 = self.addHost(
            'plc16',
            ip=IP['plc16'] + NETMASK,
            mac=MAC['plc16'])
        self.addLink(plc16, switch3)

        plc17 = self.addHost(
            'plc17',
            ip=IP['plc17'] + NETMASK,
            mac=MAC['plc17'])
        self.addLink(plc17, switch3)

        plc18 = self.addHost(
            'plc18',
            ip=IP['plc18'] + NETMASK,
            mac=MAC['plc18'])
        self.addLink(plc18, switch3)

         #Tạo host plc1
        plc19 = self.addHost(
            'plc19',
            ip=IP['plc19'] + NETMASK,
            mac=MAC['plc19'])
        #Tạo link giữa plc1 và s1
        self.addLink(plc19, switch4)

        plc20 = self.addHost(
            'plc20',
            ip=IP['plc20'] + NETMASK,
            mac=MAC['plc20'])
        self.addLink(plc20, switch4)

        plc21 = self.addHost(
            'plc21',
            ip=IP['plc21'] + NETMASK,
            mac=MAC['plc21'])
        self.addLink(plc21, switch4)

        plc22 = self.addHost(
            'plc22',
            ip=IP['plc22'] + NETMASK,
            mac=MAC['plc22'])
        self.addLink(plc22, switch4)

        plc23 = self.addHost(
            'plc23',
            ip=IP['plc23'] + NETMASK,
            mac=MAC['plc23'])
        self.addLink(plc23, switch4)

        plc24 = self.addHost(
            'plc24',
            ip=IP['plc24'] + NETMASK,
            mac=MAC['plc24'])
        self.addLink(plc24, switch4)

         #Tạo host plc1
        plc25 = self.addHost(
            'plc25',
            ip=IP['plc25'] + NETMASK,
            mac=MAC['plc25'])
        #Tạo link giữa plc1 và s1
        self.addLink(plc25, switch5)

        plc26 = self.addHost(
            'plc26',
            ip=IP['plc26'] + NETMASK,
            mac=MAC['plc26'])
        self.addLink(plc26, switch5)

        plc27 = self.addHost(
            'plc27',
            ip=IP['plc27'] + NETMASK,
            mac=MAC['plc27'])
        self.addLink(plc27, switch5)

        plc28 = self.addHost(
            'plc28',
            ip=IP['plc28'] + NETMASK,
            mac=MAC['plc28'])
        self.addLink(plc28, switch5)

        plc29 = self.addHost(
            'plc29',
            ip=IP['plc29'] + NETMASK,
            mac=MAC['plc29'])
        self.addLink(plc29, switch5)

        plc30 = self.addHost(
            'plc30',
            ip=IP['plc30'] + NETMASK,
            mac=MAC['plc30'])
        self.addLink(plc30, switch5)

         #Tạo host plc1
        plc31 = self.addHost(
            'plc31',
            ip=IP['plc31'] + NETMASK,
            mac=MAC['plc31'])
        #Tạo link giữa plc1 và s1
        self.addLink(plc31, switch6)

        plc32 = self.addHost(
            'plc32',
            ip=IP['plc32'] + NETMASK,
            mac=MAC['plc32'])
        self.addLink(plc32, switch6)

        plc33 = self.addHost(
            'plc33',
            ip=IP['plc33'] + NETMASK,
            mac=MAC['plc33'])
        self.addLink(plc33, switch6)

        plc34 = self.addHost(
            'plc34',
            ip=IP['plc34'] + NETMASK,
            mac=MAC['plc34'])
        self.addLink(plc34, switch6)

        plc35 = self.addHost(
            'plc35',
            ip=IP['plc35'] + NETMASK,
            mac=MAC['plc35'])
        self.addLink(plc35, switch6)

        plc36 = self.addHost(
            'plc36',
            ip=IP['plc36'] + NETMASK,
            mac=MAC['plc36'])
        self.addLink(plc36, switch6)

        attacker = self.addHost(
            'attacker',
            ip=IP['attacker'] + NETMASK,
            mac=MAC['attacker'])
        self.addLink(attacker, switch0)