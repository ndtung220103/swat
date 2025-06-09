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
        plc1, plc2, plc3, plc4, plc5, plc6, s1, hmi, plc7, plc8, plc9, plc10, plc11, plc12, plc13, plc14, plc15, plc16, plc17, plc18\
        , plc19, plc20, plc21, plc22, plc23, plc24 , plc25, plc26, plc27, plc28, plc29, plc30\
            , plc31, plc32, plc33, plc34, plc35, plc36= self.net.get(
            'plc1', 'plc2', 'plc3', 'plc4', 'plc5', 'plc6', 's1', 'hmi','plc7', 'plc8', 'plc9', 'plc10', 'plc11', 'plc12'
                ,'plc13', 'plc14', 'plc15', 'plc16', 'plc17', 'plc18','plc19', 'plc20', 'plc21', 'plc22', 'plc23', 'plc24'
                ,'plc25', 'plc26', 'plc27', 'plc28', 'plc29', 'plc30','plc31', 'plc32', 'plc33', 'plc34', 'plc35', 'plc36')
        
        # SPHINX_SWAT_TUTORIAL RUN(
        plc36.cmd(sys.executable + ' -u ' + ' plc36.py  &> logs/plc36.log &')
        plc35.cmd(sys.executable + ' -u ' + ' plc35.py  &> logs/plc35.log &')
        plc34.cmd(sys.executable + ' -u ' + ' plc34.py  &> logs/plc34.log &')
        plc33.cmd(sys.executable + ' -u ' + ' plc33.py  &> logs/plc33.log &')
        plc32.cmd(sys.executable + ' -u ' + ' plc32.py  &> logs/plc32.log &')
        plc31.cmd(sys.executable + ' -u ' + ' plc31.py  &> logs/plc31.log &')
        plc30.cmd(sys.executable + ' -u ' + ' plc30.py  &> logs/plc30.log &')
        plc29.cmd(sys.executable + ' -u ' + ' plc29.py  &> logs/plc29.log &')
        plc28.cmd(sys.executable + ' -u ' + ' plc28.py  &> logs/plc28.log &')
        plc27.cmd(sys.executable + ' -u ' + ' plc27.py  &> logs/plc27.log &')
        plc26.cmd(sys.executable + ' -u ' + ' plc26.py  &> logs/plc26.log &')
        plc25.cmd(sys.executable + ' -u ' + ' plc25.py  &> logs/plc25.log &')
        plc24.cmd(sys.executable + ' -u ' + ' plc24.py  &> logs/plc24.log &')
        plc23.cmd(sys.executable + ' -u ' + ' plc23.py  &> logs/plc23.log &')
        plc22.cmd(sys.executable + ' -u ' + ' plc22.py  &> logs/plc22.log &')
        plc21.cmd(sys.executable + ' -u ' + ' plc21.py  &> logs/plc21.log &')
        plc20.cmd(sys.executable + ' -u ' + ' plc20.py  &> logs/plc20.log &')
        plc19.cmd(sys.executable + ' -u ' + ' plc19.py  &> logs/plc19.log &')
        plc18.cmd(sys.executable + ' -u ' + ' plc18.py  &> logs/plc18.log &')
        plc17.cmd(sys.executable + ' -u ' + ' plc17.py  &> logs/plc17.log &')
        plc16.cmd(sys.executable + ' -u ' + ' plc16.py  &> logs/plc16.log &')
        plc15.cmd(sys.executable + ' -u ' + ' plc15.py  &> logs/plc15.log &')
        plc14.cmd(sys.executable + ' -u ' + ' plc14.py  &> logs/plc14.log &')
        plc13.cmd(sys.executable + ' -u ' + ' plc13.py  &> logs/plc13.log &')
        plc12.cmd(sys.executable + ' -u ' + ' plc12.py  &> logs/plc12.log &')
        plc11.cmd(sys.executable + ' -u ' + ' plc11.py  &> logs/plc11.log &')
        plc10.cmd(sys.executable + ' -u ' + ' plc10.py  &> logs/plc10.log &')
        plc9.cmd(sys.executable + ' -u ' + ' plc9.py  &> logs/plc9.log &')
        plc8.cmd(sys.executable + ' -u ' + ' plc8.py  &> logs/plc8.log &')
        plc7.cmd(sys.executable + ' -u ' + ' plc7.py  &> logs/plc7.log &')
        plc6.cmd(sys.executable + ' -u ' + ' plc6.py  &> logs/plc6.log &')
        plc5.cmd(sys.executable + ' -u ' + ' plc5.py  &> logs/plc5.log &')
        plc4.cmd(sys.executable + ' -u ' + ' plc4.py  &> logs/plc4.log &')
        plc3.cmd(sys.executable + ' -u ' + ' plc3.py  &> logs/plc3.log &')
        plc2.cmd(sys.executable + ' -u ' + ' plc2.py  &> logs/plc2.log &')
        plc1.cmd(sys.executable + ' -u ' + ' plc1.py  &> logs/plc1.log &')
        hmi.cmd(sys.executable + ' -u ' + ' hmi.py  &> logs/ht6-mi.log &')
        s1.cmd(sys.executable + ' -u ' + ' Raw_Water_Tank.py  &> logs/Raw_Water_Tank.log &')
        s1.cmd(sys.executable + ' -u ' + ' UF_Feed_Tank.py  &> logs/UF_Feed_Tank.log &')
        s1.cmd(sys.executable + ' -u ' + ' RO_Feed_Tank.py  &> logs/RO_Feed_Tank.log &')
        s1.cmd(sys.executable + ' -u ' + ' Raw_Permeate_Tank.py  &> logs/Raw_Permeate_Tank.log &')
        s1.cmd(sys.executable + ' -u ' + ' UF_backwash_Tank.py  &> logs/UF_backwash_Tank.log &')

        # SPHINX_SWAT_TUTORIAL RUN)
        CLI(self.net)

        net.stop()

if __name__ == "__main__":

    topo = SwatTopo()
    #controller = RemoteController('pox', ip='127.0.0.1', port=6633)
    net = Mininet(topo=topo)

    swat_cps = SwatCPS(
        name='swat',
        net=net)