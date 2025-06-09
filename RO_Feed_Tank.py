"""
SWaT sub1 physical process

RawWaterTank has an inflow pipe and outflow pipe, both are modeled according
to the equation of continuity from the domain of hydraulics
(pressurized liquids) and a drain orefice modeled using the Bernoulli's
principle (for the trajectories).
"""


from minicps.devices import Tank

from utils import PUMP_FLOWRATE_OUT_T3, PUMP_FLOWRATE_OUT_T4, PUMP_FLOWRATE_BACKWASH
from utils import TANK_HEIGHT, TANK_SECTION, TANK_DIAMETER
from utils import LIT_401_M
from utils import STATE, PP_PERIOD_SEC, PP_PERIOD_HOURS, PP_SAMPLES


import sys
import time


# SPHINX_SWAT_TUTORIAL TAGS(
P301 = ('P301', 3)
P401 = ('P401', 4)
P602 = ('P602', 6)
LIT401 = ('LIT401', 4)
LIT301 = ('LIT301', 3)
FIT301 = ('FIT301', 3)
FIT401 = ('FIT401', 4)
# SPHINX_SWAT_TUTORIAL TAGS)


# TODO: implement orefice drain with Bernoulli/Torricelli formula
class ROFEEDTank(Tank):

    def pre_loop(self):

        # SPHINX_SWAT_TUTORIAL STATE INIT(
        self.set(P401, 0)
        self.level = self.set(LIT401, 0.000)
        # SPHINX_SWAT_TUTORIAL STATE INIT)

    def main_loop(self):

        count = 0
        timestamp=0
        while True:

            new_level = self.level

            # compute water volume
            water_volume = self.section * new_level

            p301 = self.get(P301)
            if int(p301) == 1:
                inflow = PUMP_FLOWRATE_OUT_T3 * PP_PERIOD_HOURS
                water_volume += inflow
            else:
                self.set(FIT301, 0.00)

            p602 = self.get(P602)
            if int(p602) == 1:
                washflow = PUMP_FLOWRATE_BACKWASH * PP_PERIOD_HOURS
                water_volume += washflow
            

            # outflow
            p401 = self.get(P401)
            if int(p401) == 1:
                self.set(FIT401, PUMP_FLOWRATE_OUT_T4)
                outflow = PUMP_FLOWRATE_OUT_T4 * PP_PERIOD_HOURS
                # print("DEBUG RawWaterTank inflow: ", inflow)
                water_volume -= outflow
            else:
                self.set(FIT401, 0.00)


            # compute new water_level
            new_level = water_volume / self.section

            # level cannot be negative
            if new_level <= 0.0:
                new_level = 0.0

            # update internal and state water level
            print("DEBUG new_level: %.5f \t delta: %.5f" % (
                new_level, new_level - self.level))
            self.level = self.set(LIT401, new_level)

            count += 1
            time.sleep(PP_PERIOD_SEC)
            timestamp+=PP_PERIOD_SEC


if __name__ == '__main__':

    rwt = ROFEEDTank(
        name='rft',
        state=STATE,
        protocol=None,
        section=TANK_SECTION,
        level=0.000
    )