from minicps.devices import HMI
from utils import HMI_PROTOCOL, STATE
import time
import socket
import json

MV101 = ('MV101', 1)
LIT101 = ('LIT101', 1)
P101 = ('P101', 1)
MV201 = ('MV201', 2)
LIT301 = ('LIT301', 3)
P301 = ('P301', 3)
LIT401 = ('LIT401', 4)
P401 = ('P401', 4)
P501 = ('P501', 5)
LIT501 = ('LIT501', 5)
LIT502 = ('LIT502', 5)
P602 = ('P602', 6)

POX_HOST = '127.0.0.1'  # địa chỉ máy chạy POX controller
POX_PORT = 9999         # cổng mà POX controller lắng nghe

class MyHMI(HMI):

    def send_to_controller(self, data_dict):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((POX_HOST, POX_PORT))
                s.sendall(json.dumps(data_dict).encode())
        except Exception as e:
            print(f"[Socket Error] {e}")

    def main_loop(self, sleep=1):
        time.sleep(5)
        while True:
            try:
                data = {
                    'MV101': int(self.get(MV101)),
                    'LIT101': float(self.get(LIT101)),
                    'P101': int(self.get(P101)),
                    'MV201': int(self.get(MV201)),
                    'LIT301': float(self.get(LIT301)),
                    'P301': int(self.get(P301)),
                    'LIT401': float(self.get(LIT401)),
                    'P401': int(self.get(P401)),
                    'P501': int(self.get(P501)),
                    'LIT501': float(self.get(LIT501)),
                    'LIT502': float(self.get(LIT502)),
                    'P602': int(self.get(P602)),
                }
                print(f"[HMI] Sending data: {data}")
                self.send_to_controller(data)
            except Exception as e:
                print(f"[HMI Error] can't connect to PLC: {e}")
            time.sleep(sleep)

if __name__ == "__main__":
    hmi = MyHMI(
        name="hmi",
        protocol=HMI_PROTOCOL,
        state=STATE
    )
    hmi.main_loop()
