"""
swat plc6.py
"""

from minicps.devices import PLC
from utils import PLC6_DATA, STATE, PLC6_PROTOCOL
from utils import PLC_PERIOD_SEC, PLC_SAMPLES
from utils import IP, LIT_502_M , LIT_501_M

import time

PLC6_ADDR = IP['plc6']
PLC5_ADDR = IP['plc5']


LIT501 = ('LIT501', 5)
LIT502 = ('LIT502', 5)
P602 = ('P602', 6)
P501 = ('P501', 5)


# TODO: real value tag where to read/write flow sensor
class SwatPLC6(PLC):

    def pre_loop(self, sleep=0.2):
        print('DEBUG: swat plc6 enters pre_loop')

        time.sleep(sleep)

    def main_loop(self):

        print('DEBUG: swat plc6 enters main_loop.')

        count = 1
        wash = 5
        while(count <= PLC_SAMPLES):

            lit501 = float(self.get(LIT501))
            print('DEBUG plc6 lit501: %.5f' % lit501)
            self.send(LIT501, lit501, PLC6_ADDR)
            if lit501 >= LIT_501_M['HH']:
                print("WARNING PLC6 - lit501 over HH: %.2f >= %.2f." % (
                    lit501, LIT_501_M['HH']))
            if lit501 >= LIT_501_M['H']:
                print("INFO PLC6 - lit501 over H ")
            elif lit501 <= LIT_501_M['LL']:
                print("WARNING PLC6 - lit501 under LL: %.2f <= %.2f." % (
                    lit501, LIT_501_M['LL']))
            elif lit501 <= LIT_501_M['L']:
                print("INFO PLC6 - lit501 under L")


            lit502 = float(self.get(LIT502))
            print('DEBUG plc6 lit502: %.5f' % lit502)
            self.send(LIT502, lit502, PLC6_ADDR)
            if lit502 >= LIT_502_M['HH']:
                print("WARNING PLC6 - lit502 over HH: %.2f >= %.2f." % (
                    lit502, LIT_502_M['HH']))
            if lit502 >= LIT_502_M['H']:
                print("INFO PLC6 - lit502 over H ")
            elif lit502 <= LIT_502_M['LL']:
                print("WARNING PLC6 - lit502 under LL: %.2f <= %.2f." % (
                    lit502, LIT_502_M['LL']))
            elif lit502 <= LIT_502_M['L']:
                print("INFO PLC6 - lit502 under L")

            if count % 45 == 0 :
                wash = 0
            if wash < 3 and lit502 >= LIT_502_M['LL'] :
                self.set(P602, 1)
                self.send(P602, 1, PLC6_ADDR)
            else:
                self.set(P602, 0)
                self.send(P602, 0, PLC6_ADDR)
            wash += 1
            count += 1
            time.sleep(PLC_PERIOD_SEC)
            

        print('DEBUG swat plc6 shutdown')


if __name__ == "__main__":

    # notice that memory init is different form disk init
    plc6 = SwatPLC6(
        name='plc6',
        state=STATE,
        protocol=PLC6_PROTOCOL,
        memory=PLC6_DATA,
        disk=PLC6_DATA)