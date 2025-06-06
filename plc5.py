"""
swat plc5.py
"""

from minicps.devices import PLC
from utils import PLC5_DATA, STATE, PLC5_PROTOCOL
from utils import PLC_PERIOD_SEC, PLC_SAMPLES
from utils import IP

import time

PLC4_ADDR = IP['plc4']
PLC5_ADDR = IP['plc5']

P501 = ('P501', 5)
P401 = ('P401', 4)

# TODO: real value tag where to read/write flow sensor
class SwatPLC5(PLC):

    def pre_loop(self, sleep=0.2):
        print('DEBUG: plc5 enters pre_loop')

        time.sleep(sleep)

    def main_loop(self):
        """plc1 main loop.

            - reads sensors value
            - drives actuators according to the control strategy
            - updates its enip server
        """

        print('DEBUG: swat plc5 enters main_loop.')

        count = 0
        while True: 
            try:          
                p501 = int(self.receive(P501, PLC5_ADDR))
                self.set(P501, p501)
                print('DEBUG plc5 p501',p501)
            except Exception as e:
                print(f"Failed to receive data from PLC: {e}")
            time.sleep(PLC_PERIOD_SEC)
            count += 1

if __name__ == "__main__":

    # notice that memory init is different form disk init
    plc5 = SwatPLC5(
        name='plc5',
        state=STATE,
        protocol=PLC5_PROTOCOL,
        memory=PLC5_DATA,
        disk=PLC5_DATA)