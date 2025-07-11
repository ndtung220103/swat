"""
SWaT sub1 physical process

RawWaterTank has an inflow pipe and outflow pipe, both are modeled according
to the equation of continuity from the domain of hydraulics
(pressurized liquids) and a drain orefice modeled using the Bernoulli's
principle (for the trajectories).
"""


from minicps.devices import Tank

from utils import PUMP_FLOWRATE_IN, PUMP_FLOWRATE_OUT
from utils import TANK_HEIGHT, TANK_SECTION, TANK_DIAMETER
from utils import LIT_101_M, RWT_INIT_LEVEL
from utils import STATE, PP_PERIOD_SEC, PP_PERIOD_HOURS, PP_SAMPLES
#import pandas as pd

import sys
import time


# SPHINX_SWAT_TUTORIAL TAGS(
MV101 = ('MV101', 1)
MV201 = ('MV201', 2)
P101 = ('P101', 1)
LIT101 = ('LIT101', 1)
LIT301 = ('LIT301', 3)
FIT101 = ('FIT101', 1)
FIT201 = ('FIT201', 2)
# SPHINX_SWAT_TUTORIAL TAGS)


# TODO: implement orefice drain with Bernoulli/Torricelli formula
class RawWaterTank(Tank):

    def pre_loop(self):

        # SPHINX_SWAT_TUTORIAL STATE INIT(
        self.set(MV101, 1)
        self.set(P101, 0)
        self.set(MV201, 1)
        self.level = self.set(LIT101, 0.800)
        # SPHINX_SWAT_TUTORIAL STATE INIT)

        # test underflow
        # self.set(MV101, 0)
        # self.set(P101, 1)
        # self.level = self.set(LIT101, 0.500)

    def main_loop(self):

        count = 0
        #columns = ['Time', 'MV101', 'P101', 'LIT101', 'LIT301', 'FIT101', 'FIT201']
       # df = pd.DataFrame(columns=columns)
        timestamp=0
        while True:

            new_level = self.level

            # compute water volume
            water_volume = self.section * new_level

            # inflows volumes
            mv101 = self.get(MV101)
            print('mv01 ',int(mv101))
            if int(mv101) == 1:
                self.set(FIT101, PUMP_FLOWRATE_IN)
                inflow = PUMP_FLOWRATE_IN * PP_PERIOD_HOURS
                # print("DEBUG RawWaterTank inflow: ", inflow)
                water_volume += inflow
            else:
                self.set(FIT101, 0.00)

            # outflows volumes
            p101 = self.get(P101)
            print('p101 ',int(p101))
            if int(p101) == 1:
                self.set(FIT201, PUMP_FLOWRATE_OUT)
                outflow = PUMP_FLOWRATE_OUT * PP_PERIOD_HOURS
                # print("DEBUG RawWaterTank outflow: ", outflow)
                water_volume -= outflow
            else:
                self.set(FIT201, 0.00)

            # compute new water_level
            new_level = water_volume / self.section

            # level cannot be negative
            if new_level <= 0.0:
                new_level = 0.0

            # update internal and state water level
            print("DEBUG new_level: %.5f \t delta: %.5f" % (
                new_level, new_level - self.level))
            self.level = self.set(LIT101, new_level)
 
            #new_data = pd.DataFrame(data = [[timestamp, self.get(MV101), self.get(P101), self.get(LIT101), self.get(LIT301), self.get(FIT101), self.get(FIT201)]], columns=columns)
            #df = pd.concat([df,new_data])
            #df.to_csv('logs/data.csv', index=False)
            count += 1
            time.sleep(PP_PERIOD_SEC)
            timestamp+=PP_PERIOD_SEC


if __name__ == '__main__':

    rwt = RawWaterTank(
        name='rwt',
        state=STATE,
        protocol=None,
        section=TANK_SECTION,
        level=RWT_INIT_LEVEL
    )