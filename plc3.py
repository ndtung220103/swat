
"""
swat plc3
"""

from minicps.devices import PLC
from utils import PLC3_DATA, STATE, PLC3_PROTOCOL
from utils import PLC_SAMPLES, PLC_PERIOD_SEC, LIT_301_M, LIT_401_M
from utils import IP

import time

PLC4_ADDR = IP['plc4']
PLC2_ADDR = IP['plc2']
PLC3_ADDR = IP['plc3']

LIT301_3 = ('LIT301', 3)
LIT401 = ('LIT401', 4)
P301 = ('P301', 3)

class SwatPLC3(PLC):

    def pre_loop(self, sleep=0.2):
        print('DEBUG: swat plc3 enters pre_loop')

        time.sleep(sleep)

    def main_loop(self):
        """plc3 main loop.

            - read UF tank level from the sensor
            - update internal enip server
        """

        print('DEBUG: swat plc3 enters main_loop.')

        count = 0
        while(count <= PLC_SAMPLES):

            lit301 = float(self.get(LIT301_3))
            print("DEBUG PLC3 - get lit301: %f" % lit301)

            self.send(LIT301_3, lit301, PLC3_ADDR)

            if lit301 >= LIT_301_M['HH']:
                print("WARNING PLC1 - lit301 over HH: %.2f >= %.2f." % (
                    lit301, LIT_301_M['HH']))

            if lit301 >= LIT_301_M['H']:
                print("INFO PLC1 - lit301 over H ")
                

            elif lit301 <= LIT_301_M['LL']:
                print("WARNING PLC1 - lit301 under LL: %.2f <= %.2f." % (
                    lit301, LIT_301_M['LL']))

                # CLOSE p101
                print("INFO PLC3 - close p301.")
                self.set(P301, 0)
                self.send(P301, 0, PLC3_ADDR)

            elif lit301 <= LIT_301_M['L']:
                print("INFO PLC1 - lit301 under L ")
                

            # # read from PLC4
            lit401 = float(self.receive(LIT401, PLC4_ADDR))
            print("DEBUG PLC3 - receive lit401: %f" % lit401)

            if  lit401 >= LIT_401_M['H'] :
                # CLOSE p101
                self.set(P301, 0)
                self.send(P301, 0, PLC3_ADDR)
                print("INFO PLC4" \
                      "or over LIT_401_M['H']: -> close p301.")

            elif lit401 <= LIT_401_M['L'] and lit301 >= LIT_301_M['LL']:
                # OPEN p301
                self.set(P301, 1)
                self.send(P301, 1, PLC3_ADDR)
                print("INFO PLC4 - lit401 under LIT_301_M['L'] -> open p101.")




            time.sleep(PLC_PERIOD_SEC)
            count += 1

        print('DEBUG swat plc3 shutdown')


if __name__ == "__main__":

    # notice that memory init is different form disk init
    plc3 = SwatPLC3(
        name='plc3',
        state=STATE,
        protocol=PLC3_PROTOCOL,
        memory=PLC3_DATA,
        disk=PLC3_DATA)