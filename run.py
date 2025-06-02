"""
swat run.py
"""

from mininet.net import Mininet
from mininet.cli import CLI
from minicps.mcps import MiniCPS
from mininet.node import RemoteController, OVSSwitch
from mininet.link import Intf
from topo import SwatTopo

import sys
import os


class SwatCPS(MiniCPS):

    """Main container used to run the simulation."""

    def __init__(self, name, net):

        self.name = name
        self.net = net

        net.start()

        net.pingAll()

        # start devices
        plc1, plc2, plc3, plc4, plc5, plc6, s1, hmi = self.net.get(
            'plc1', 'plc2', 'plc3', 'plc4', 'plc5', 'plc6', 's1', 'hmi')
        
        os.system("ip link show veth0 || ip link add veth0 type veth peer name veth1")

        # 2. Kích hoạt veth0
        os.system("ip link set veth0 up")

        # 3. Gán IP cho veth0 trên hệ điều hành VM (phía ngoài Mininet)
        os.system("ip addr add 10.0.3.10/24 dev veth0 || true")

        # 4. Gắn veth1 vào node hmi trong Mininet
        Intf('veth1', node=hmi)
        hmi.cmd('ifconfig veth1 10.0.3.20/24 up')

        # SPHINX_SWAT_TUTORIAL RUN(
        plc2.cmd(sys.executable + ' -u ' + ' plc2.py  &> logs/plc2.log &')
        plc3.cmd(sys.executable + ' -u ' + ' plc3.py  &> logs/plc3.log &')
        plc4.cmd(sys.executable + ' -u ' + ' plc4.py  &> logs/plc4.log &')
        plc5.cmd(sys.executable + ' -u ' + ' plc5.py  &> logs/plc5.log &')
        plc6.cmd(sys.executable + ' -u ' + ' plc6.py  &> logs/plc6.log &')
        plc1.cmd(sys.executable + ' -u ' + ' plc1.py  &> logs/plc1.log &')
        s1.cmd(sys.executable + ' -u ' + ' Raw_Water_Tank.py  &> logs/Raw_Water_Tank.log &')
        s1.cmd(sys.executable + ' -u ' + ' UF_Feed_Tank.py  &> logs/UF_Feed_Tank.log &')
        s1.cmd(sys.executable + ' -u ' + ' RO_Feed_Tank.py  &> logs/RO_Feed_Tank.log &')
        s1.cmd(sys.executable + ' -u ' + ' Raw_Permeate_Tank.py  &> logs/Raw_Permeate_Tank.log &')
        s1.cmd(sys.executable + ' -u ' + ' UF_backwash_Tank.py  &> logs/UF_backwash_Tank.log &')
        hmi.cmd(sys.executable + ' -u ' + ' hmi.py  &> logs/hmi.log &')

        # SPHINX_SWAT_TUTORIAL RUN)
        CLI(self.net)

        net.stop()

if __name__ == "__main__":

    topo = SwatTopo()
    controller = RemoteController('pox', ip='127.0.0.1', port=6633)
    net = Mininet(topo=topo, controller=controller)

    swat_cps = SwatCPS(
        name='swat',
        net=net)