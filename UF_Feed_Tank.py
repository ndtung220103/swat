"""
SWaT sub1 physical process

RawWaterTank has an inflow pipe and outflow pipe, both are modeled according
to the equation of continuity from the domain of hydraulics
(pressurized liquids) and a drain orefice modeled using the Bernoulli's
principle (for the trajectories).
"""


from minicps.devices import Tank

from utils import PUMP_FLOWRATE_OUT_T3, PUMP_FLOWRATE_OUT
from utils import TANK_HEIGHT, TANK_SECTION, TANK_DIAMETER
from utils import LIT_301_M
from utils import STATE, PP_PERIOD_SEC, PP_PERIOD_HOURS, PP_SAMPLES


import sys
import time


# SPHINX_SWAT_TUTORIAL TAGS(
MV201 = ('MV201', 2)
P301 = ('P301', 3)
P101 = ('P101', 1)
LIT401 = ('LIT401', 4)
LIT301 = ('LIT301', 3)
FIT301 = ('FIT301', 3)
FIT201 = ('FIT201', 2)
# SPHINX_SWAT_TUTORIAL TAGS)


# TODO: implement orefice drain with Bernoulli/Torricelli formula
class UFFEEDTank(Tank):

    def pre_loop(self):

        # SPHINX_SWAT_TUTORIAL STATE INIT(
        self.set(MV201, 1)
        self.set(P301, 0)
        self.level = self.set(LIT301, 0.000)
        # SPHINX_SWAT_TUTORIAL STATE INIT)

    def main_loop(self):

        count = 0
        timestamp=0
        while True:

            new_level = self.level

            # compute water volume
            water_volume = self.section * new_level

            p101 = self.get(P101)
            if int(p101) == 1:
                inflow = PUMP_FLOWRATE_OUT * PP_PERIOD_HOURS
                # print("DEBUG RawWaterTank outflow: ", outflow)
                water_volume += inflow
            else:
                self.set(FIT201, 0.00)


            # outflow
            p301 = self.get(P301)
            if int(p301) == 1:
                self.set(FIT301, PUMP_FLOWRATE_OUT_T3)
                outflow = PUMP_FLOWRATE_OUT_T3 * PP_PERIOD_HOURS
                # print("DEBUG RawWaterTank inflow: ", inflow)
                water_volume -= outflow
            else:
                self.set(FIT301, 0.00)


            # compute new water_level
            new_level = water_volume / self.section

            # level cannot be negative
            if new_level <= 0.0:
                new_level = 0.0

            # update internal and state water level
            print("DEBUG new_level: %.5f \t delta: %.5f" % (
                new_level, new_level - self.level))
            self.level = self.set(LIT301, new_level)

            count += 1
            time.sleep(PP_PERIOD_SEC)
            timestamp+=PP_PERIOD_SEC


if __name__ == '__main__':

    rwt = UFFEEDTank(
        name='uft',
        state=STATE,
        protocol=None,
        section=TANK_SECTION,
        level=0.000
    )