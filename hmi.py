from minicps.devices import HMI
from utils import HMI_PROTOCOL, STATE
from utils import PLC_PERIOD_SEC, PLC_SAMPLES
from utils import IP, LIT_101_M, LIT_301_M, LIT_401_M, LIT_501_M, LIT_502_M
import time
import socket
import json

PLC1_ADDR = IP['plc1']
PLC2_ADDR = IP['plc2']
PLC3_ADDR = IP['plc3']
PLC4_ADDR = IP['plc4']
PLC5_ADDR = IP['plc5']
PLC6_ADDR = IP['plc6']
# Danh sách tag
MV101 =  ('MV101',    1)
LIT101 =    ('LIT101',   1)
P101 =    ('P101',     1)
MV201 =    ('MV201',    2)
LIT301 =    ('LIT301',   3)
P301 =     ('P301',   3)
LIT401 =     ('LIT401',   4)
P401 =    ('P401',   4)
P501 =    ('P501',   5)
LIT501 =    ('LIT501',   5)
LIT502 =    ('LIT502',   5)
P602 =     ('P602',   6)

CONTROLLER_IP = '10.0.3.10'
CONTROLLER_PORT = 9999

class MyHMI(HMI):

    def main_loop(self, sleep=1):
        time.sleep(5)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        count = 1
        wash = 5
        while True:
            try:
                #plc1 handle lit101
                lit101 = float(self.receive(LIT101, PLC1_ADDR))
                if lit101 >= LIT_101_M['HH']:
                    print("WARNING PLC1 - lit101 over HH: %.2f >= %.2f." % (
                        lit101, LIT_101_M['HH']))

                if lit101 >= LIT_101_M['H']:
                    # CLOSE mv101
                    print("INFO PLC1 - lit101 over H -> close mv101.")
                    self.send(MV101, 0, PLC1_ADDR)
                    
                elif lit101 <= LIT_101_M['LL']:
                    print("WARNING PLC1 - lit101 under LL: %.2f <= %.2f." % (
                        lit101, LIT_101_M['LL']))
                    # CLOSE p101
                    print("INFO PLC1 - close p101.")
                    self.send(P101, 0, PLC1_ADDR)

                elif lit101 <= LIT_101_M['L']:
                    # OPEN mv101
                    print("INFO PLC1 - lit101 under L -> open mv101.")
                    self.send(MV101, 1, PLC1_ADDR)
                
                # Handle lit301 
                lit301 = float(self.receive(LIT301, PLC3_ADDR))
                print("DEBUG PLC1 - receive lit301: %f" % lit301)
                mv201 = int(self.receive(MV201, PLC2_ADDR))
                if  lit301 >= LIT_301_M['H'] or mv201 == 0:
                    # CLOSE p101
                    self.send(P101, 0, PLC1_ADDR)
                    print("INFO PLC1 - fit201 under FIT_201_THRESH " \
                        "or over LIT_301_M['H']: -> close p101.")

                elif lit301 <= LIT_301_M['L'] and mv201 == 1 and lit101 >= LIT_101_M['LL']:
                    # OPEN p101
                    self.send(P101, 1, PLC1_ADDR)
                    print("INFO PLC1 - lit301 under LIT_301_M['L'] -> open p101.")

                #plc2
                lit301 = float(self.receive(LIT301, PLC3_ADDR))
                if lit301 >= LIT_301_M['HH']:
                    print("WARNING PLC3 - lit301 over HH: %.2f >= %.2f." % (
                        lit301, LIT_301_M['HH']))

                if lit301 >= LIT_301_M['H']:
                    print("INFO PLC3 - lit301 over H -> close mv201.")
                    self.send(MV201, 0, PLC2_ADDR)

                elif lit301 <= LIT_301_M['L']:
                    # OPEN mv101
                    print("INFO PLC3 - lit301 under L -> open mv201.")
                    self.send(MV201, 1, PLC2_ADDR)

                #plc3
                lit301 = float(self.receive(LIT301, PLC3_ADDR))
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
                    self.send(P301, 0, PLC3_ADDR)

                elif lit301 <= LIT_301_M['L']:
                    print("INFO PLC1 - lit301 under L ")
                    
                # # read from PLC4
                lit401 = float(self.receive(LIT401, PLC4_ADDR))
                print("DEBUG PLC3 - receive lit401: %f" % lit401)

                if  lit401 >= LIT_401_M['H'] :
                    self.send(P301, 0, PLC3_ADDR)
                    print("INFO PLC4" \
                        "or over LIT_401_M['H']: -> close p301.")

                elif lit401 <= LIT_401_M['L'] and lit301 >= LIT_301_M['LL']:
                    self.send(P301, 1, PLC3_ADDR)
                    print("INFO PLC4 - lit401 under LIT_301_M['L'] -> open p101.")

                #plc4
                if lit401 >= LIT_401_M['HH']:
                    print("WARNING PLC4 - lit401 over HH: %.2f >= %.2f." % (
                        lit401, LIT_401_M['HH']))

                if lit401 >= LIT_401_M['H']:
                    print("INFO PLC4 - lit401 over H ")

                elif lit401 <= LIT_401_M['LL']:
                    print("WARNING PLC4 - lit401 under LL: %.2f <= %.2f." % (
                        lit401, LIT_401_M['LL']))
                    print("INFO PLC4 - close p401.")
                    self.send(P401, 0, PLC4_ADDR)

                elif lit401 <= LIT_401_M['L']:
                    print("INFO PLC4 - lit401 under L ")
                if lit401 >= LIT_401_M['L']:
                    print("INFO PLC4 - open p401.")
                    self.send(P401, 1, PLC4_ADDR)

                #plc5
                p401 = int(self.receive(P401, PLC4_ADDR))
                self.send(P501, p401, PLC5_ADDR)

                #plc6
                lit501 = float(self.receive(LIT501,PLC6_ADDR))
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

                lit502 = float(self.receive(LIT502,PLC6_ADDR))
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
                    self.send(P602, 1, PLC6_ADDR)
                else:
                    self.send(P602, 0, PLC6_ADDR)
                wash += 1
                count += 1

            except Exception as e:
                print(f"Failed to receive data from PLC: {e}")
            try:
                data = {
                    'LIT101': lit101,
                    'LIT301': lit301,
                    'LIT401': lit401,
                    'LIT501': lit501,
                    'LIT502': lit502
                }

                message = json.dumps(data)
                sock.sendto(message.encode(), (CONTROLLER_IP, CONTROLLER_PORT))
                print(f"Sent sensor data to controller: {data}")
            except Exception as e:
                print(f"Failed to send data to controller: {e}")
            time.sleep(PLC_PERIOD_SEC)

if __name__ == "__main__":
    hmi = MyHMI(
        name="hmi",
        protocol=HMI_PROTOCOL,
        state=STATE
    )
    hmi.main_loop()
