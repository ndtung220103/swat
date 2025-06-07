"""
SWaT sub1 physical process

RawWaterTank has an inflow pipe and outflow pipe, both are modeled according
to the equation of continuity from the domain of hydraulics
(pressurized liquids) and a drain orefice modeled using the Bernoulli's
principle (for the trajectories).
"""


from minicps.devices import Tank

from utils import PUMP_FLOWRATE_IN_T52, PUMP_FLOWRATE_BACKWASH
from utils import TANK_HEIGHT, TANK_SECTION, TANK_DIAMETER
from utils import LIT_502_M
from utils import STATE, PP_PERIOD_SEC, PP_PERIOD_HOURS, PP_SAMPLES

import sys
import time


# SPHINX_SWAT_TUTORIAL TAGS(
P501 = ('P501', 5)
LIT502 = ('LIT502', 5)
FIT502 = ('FIT502', 5)
FIT602 = ('FIT602', 6)
P602 = ('P602',6)
# SPHINX_SWAT_TUTORIAL TAGS)


# TODO: implement orefice drain with Bernoulli/Torricelli formula
class UFBACKWASHTank(Tank):

    def pre_loop(self):

        # SPHINX_SWAT_TUTORIAL STATE INIT(
        self.level = self.set(LIT502, 0.000)
        # SPHINX_SWAT_TUTORIAL STATE INIT)

        # test underflow
        # self.set(MV101, 0)
        # self.set(P101, 1)
        # self.level = self.set(LIT101, 0.500)

    def main_loop(self):

        count = 0
        timestamp=0
        while True:

            new_level = self.level

            # compute water volume
            water_volume = self.section * new_level

            # inflows volumes
            p501 = self.get(P501)
            if int(p501) == 1:
                self.set(FIT502, PUMP_FLOWRATE_IN_T52)
                inflow = PUMP_FLOWRATE_IN_T52 * PP_PERIOD_HOURS
                # print("DEBUG RawWaterTank inflow: ", inflow)
                water_volume += inflow
            else:
                self.set(FIT502, 0.00)

            # outflows volumes
            p602 = self.get(P602)
            if int(p602) == 1:
                self.set(FIT602, PUMP_FLOWRATE_BACKWASH)
                outflow = PUMP_FLOWRATE_BACKWASH * PP_PERIOD_HOURS
                print("DEBUG BackwashTank outflow: ", outflow)
                water_volume -= outflow
            else:
                self.set(FIT602, 0.00)

            # compute new water_level
            new_level = water_volume / self.section

            # level cannot be negative
            if new_level <= 0.0:
                new_level = 0.0

            # update internal and state water level
            print("DEBUG new_level: %.5f \t delta: %.5f" % (
                new_level, new_level - self.level))
            self.level = self.set(LIT502, new_level)

            # # 988 sec starting from 0.500 m
            # if new_level >= LIT_502_M['HH']:
            #     print('DEBUG RawWaterTank above HH count: ', count)
            #     break

            # # 367 sec starting from 0.500 m
            # elif new_level <= LIT_502_M['LL']:
            #     print('DEBUG RawWaterTank below LL count: ', count)
            #     break 
            
            count += 1
            time.sleep(PP_PERIOD_SEC)
            timestamp+=PP_PERIOD_SEC


if __name__ == '__main__':

    rwt = UFBACKWASHTank(
        name='ubt',
        state=STATE,
        protocol=None,
        section=TANK_SECTION,
        level=0.000
    )