
from minicps.devices import PLC
from utils import PLC1_DATA, STATE, PLC1_PROTOCOL
from utils import IP
from cpppo.server.enip.get_attribute import proxy


import time

PLC1_ADDR = IP['plc1']


LEVEL = ('level',)
PUMP = ('pump',)
ALERT = ('alert',)

# TODO: real value tag where to read/write flow sensor
class PLC1(PLC):

    def pre_loop(self, sleep=0.5):
        print('DEBUG:plc1 enters pre_loop')
        time.sleep(sleep)

    def main_loop(self):
        proxy(host='192.168.1.10', timeout=20.0)
        print('DEBUG: plc1 enters main_loop.')
        self.send(LEVEL, 1, PLC1_ADDR)
        self.send(PUMP, 1, PLC1_ADDR)
        self.send(ALERT, 0, PLC1_ADDR)
        while True:

            level = float(self.get(LEVEL))
            print('DEBUG plc1 level: %.5f' %level)
            #self.send(LEVEL,level , PLC1_ADDR)
            if (level < 20):
                self.send(ALERT, 0, PLC1_ADDR)
                print(f"water is normal")
            elif (level < 30):
                self.send(ALERT, 1, PLC1_ADDR)
                print(f"water is high")
            else:
                self.send(ALERT, 2, PLC1_ADDR)
                print(f"water is over")

            pump = int(self.receive(PUMP, PLC1_ADDR))
            self.set(PUMP,pump)
            print(f"pump is : {pump}")

            time.sleep(2.5)
            


if __name__ == "__main__":

    # notice that memory init is different form disk init
    plc1 = PLC1(
        name='plc1',
        state=STATE,
        protocol=PLC1_PROTOCOL,
        memory=PLC1_DATA,
        disk=PLC1_DATA)
