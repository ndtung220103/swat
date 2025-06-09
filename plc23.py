
from minicps.devices import PLC
from utils import PLC1_DATA, STATE, PLC23_PROTOCOL
from utils import PLC_PERIOD_SEC, IP

import time

PLC_ADDR = IP['plc23']


LIT101 = ('LIT101', 1)
MV101 = ('MV101', 1)

#

# TODO: real value tag where to read/write flow sensor
class SwatPLC23(PLC):

    def pre_loop(self, sleep=0.2):
        print('DEBUG: swat plc1 enters pre_loop')

        time.sleep(sleep)

    def main_loop(self):
       
        while True:
            try:
                # lit101 [meters]
                lit101 = float(self.get(LIT101))
                print('DEBUG plc1 lit101: %.5f' % lit101)
                self.send(LIT101, lit101, PLC_ADDR)

                mv101 = int(self.receive(MV101, PLC_ADDR))
                self.set(MV101, mv101)

            except Exception as e:
                print(f"Failed to receive data from PLC: {e}")
            time.sleep(PLC_PERIOD_SEC)


if __name__ == "__main__":

    # notice that memory init is different form disk init
    plc23 = SwatPLC23(
        name='plc23',
        state=STATE,
        protocol=PLC23_PROTOCOL,
        memory=PLC1_DATA,
        disk=PLC1_DATA)