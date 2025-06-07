"""
swat plc1.py
"""

from minicps.devices import PLC
from utils import PLC1_DATA, STATE, PLC1_PROTOCOL
from utils import PLC_PERIOD_SEC, PLC_SAMPLES
from utils import IP, LIT_101_M, LIT_301_M, FIT_201_THRESH

import time

PLC1_ADDR = IP['plc1']
PLC2_ADDR = IP['plc2']
PLC3_ADDR = IP['plc3']

FIT101 = ('FIT101', 1)
MV101 = ('MV101', 1)
LIT101 = ('LIT101', 1)
LIT301 = ('LIT301', 3)
P101 = ('P101', 1)
# interlocks to be received from plc2 and plc3
LIT301_1 = ('LIT301', 1)  # to be sent
LIT301_3 = ('LIT301', 3)  # to be received
FIT201_1 = ('FIT201', 1)
FIT201_2 = ('FIT201', 2)
MV201_1 = ('MV201', 1)
MV201_2 = ('MV201', 2)
#

# TODO: real value tag where to read/write flow sensor
class SwatPLC1(PLC):

    def pre_loop(self, sleep=0.2):
        print('DEBUG: swat plc1 enters pre_loop')

        time.sleep(sleep)

    def main_loop(self):
        """plc1 main loop.

            - reads sensors value
            - drives actuators according to the control strategy
            - updates its enip server
        """

        print('DEBUG: swat plc1 enters main_loop.')

        count = 0
        while True:
            try:
                # lit101 [meters]
                lit101 = float(self.get(LIT101))
                print('DEBUG plc1 lit101: %.5f' % lit101)
                self.send(LIT101, lit101, PLC1_ADDR)

                mv101 = int(self.receive(MV101, PLC1_ADDR))
                self.set(MV101, mv101)

                p101 = int(self.receive(P101, PLC1_ADDR))
                self.set(P101, p101)
            except Exception as e:
                print(f"Failed to receive data from PLC: {e}")
            time.sleep(PLC_PERIOD_SEC)
            count += 1


if __name__ == "__main__":

    # notice that memory init is different form disk init
    plc1 = SwatPLC1(
        name='plc1',
        state=STATE,
        protocol=PLC1_PROTOCOL,
        memory=PLC1_DATA,
        disk=PLC1_DATA)