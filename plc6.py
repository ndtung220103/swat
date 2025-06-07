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

        while True:
            try:
                lit501 = float(self.get(LIT501))
                print('DEBUG plc6 lit501: %.5f' % lit501)
                self.send(LIT501, lit501, PLC6_ADDR)

                lit502 = float(self.get(LIT502))
                print('DEBUG plc6 lit502: %.5f' % lit502)
                self.send(LIT502, lit502, PLC6_ADDR)
                
                p602 = int(self.receive(P602, PLC6_ADDR))
                self.set(P602, p602)
            except Exception as e:
                print(f"Failed to receive data from PLC: {e}")
            time.sleep(PLC_PERIOD_SEC)
            

if __name__ == "__main__":

    # notice that memory init is different form disk init
    plc6 = SwatPLC6(
        name='plc6',
        state=STATE,
        protocol=PLC6_PROTOCOL,
        memory=PLC6_DATA,
        disk=PLC6_DATA)