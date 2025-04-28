
"""
swat-s1 plc2
"""

from minicps.devices import PLC
from utils import PLC2_DATA, STATE, PLC2_PROTOCOL
from utils import PLC_SAMPLES, PLC_PERIOD_SEC , LIT_301_M
from utils import IP

import time

PLC1_ADDR = IP['plc1']
PLC2_ADDR = IP['plc2']
PLC3_ADDR = IP['plc3']

FIT201_2 = ('FIT201', 2)
MV201 = ('MV201', 2)
LIT301 = ('LIT301', 3)

class SwatPLC2(PLC):

    def pre_loop(self, sleep=0.1):
        print('DEBUG: swat-s1 plc2 enters pre_loop')

        time.sleep(sleep)

    def main_loop(self):
        """plc2 main loop.

            - read flow level sensors #2
            - update interal enip server
        """

        print('DEBUG: swat-s1 plc2 enters main_loop.')

        count = 0
        while(count <= PLC_SAMPLES):

            fit201 = float(self.get(FIT201_2))
            print("DEBUG PLC2 - get fit201: %f" % fit201)

            self.send(FIT201_2, fit201, PLC2_ADDR)
            
            lit301 = float(self.receive(LIT301, PLC3_ADDR))
            if lit301 >= LIT_301_M['HH']:
                print("WARNING PLC3 - lit301 over HH: %.2f >= %.2f." % (
                    lit301, LIT_301_M['HH']))

            if lit301 >= LIT_301_M['H']:
                print("INFO PLC3 - lit301 over H -> close mv201.")
                self.set(MV201, 0)
                self.send(MV201, 0, PLC2_ADDR)

            elif lit301 <= LIT_301_M['L']:
                # OPEN mv101
                print("INFO PLC3 - lit301 under L -> open mv201.")
                self.set(MV201, 1)
                self.send(MV201, 1, PLC2_ADDR)

            time.sleep(PLC_PERIOD_SEC)
            count += 1

        print('DEBUG swat plc2 shutdown')


if __name__ == "__main__":

    # notice that memory init is different form disk init
    plc2 = SwatPLC2(
        name='plc2',
        state=STATE,
        protocol=PLC2_PROTOCOL,
        memory=PLC2_DATA,
        disk=PLC2_DATA)