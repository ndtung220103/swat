"""
swat PLC4.py
"""

from minicps.devices import PLC
from utils import PLC4_DATA, STATE, PLC4_PROTOCOL
from utils import PLC_PERIOD_SEC, PLC_SAMPLES
from utils import IP, LIT_501_M, LIT_401_M

import time

PLC4_ADDR = IP['plc4']
PLC5_ADDR = IP['plc5']
PLC6_ADDR = IP['plc6']

LIT401 = ('LIT401', 4)
P401 = ('P401', 4)



# TODO: real value tag where to read/write flow sensor
class SwatPLC4(PLC):

    def pre_loop(self, sleep=0.2):
        print('DEBUG: swat plc4 enters pre_loop')

        time.sleep(sleep)

    def main_loop(self):
        """PLC4 main loop.

            - reads sensors value
            - drives actuators according to the control strategy
            - updates its enip server
        """

        print('DEBUG: swat PLC4 enters main_loop.')

        count = 0
        while True:
            try:
                lit401 = float(self.get(LIT401))
                print('DEBUG plc4 lit401 %.5f' % lit401)
                self.send(LIT401, lit401, PLC4_ADDR)

                p401 = int(self.receive(P401, PLC4_ADDR))
                self.set(P401, p401)
            except Exception as e:
                print(f"Failed to receive data from PLC: {e}")
            time.sleep(PLC_PERIOD_SEC)
            count += 1


if __name__ == "__main__":

    # notice that memory init is different form disk init
    plc4 = SwatPLC4(
        name='plc4',
        state=STATE,
        protocol=PLC4_PROTOCOL,
        memory=PLC4_DATA,
        disk=PLC4_DATA)