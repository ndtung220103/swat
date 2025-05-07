"""
swat-s1 utils.py

sqlite and enip use name (string) and pid (int) has key and the state stores
values as strings.

Actuator tags are redundant, we will use only the XXX_XXX_OPEN tag ignoring
the XXX_XXX_CLOSE with the following convention:
    - 0 = error
    - 1 = off
    - 2 = on

sqlite uses float keyword and cpppo use REAL keyword.
"""

from minicps.utils import build_debug_logger

swat = build_debug_logger(
    name=__name__,
    bytes_per_file=10000,
    rotating_files=2,
    lformat='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    ldir='logs/',
    suffix='')

# physical process {{{1
# SPHINX_SWAT_TUTORIAL PROCESS UTILS(
GRAVITATION = 9.81             # m.s^-2
TANK_DIAMETER = 1.38           # m
TANK_SECTION = 1.5             # m^2
PUMP_FLOWRATE_IN = 2.55        # m^3/h spec say btw 2.2 and 2.4
PUMP_FLOWRATE_OUT = 2.45       # m^3/h spec say btw 2.2 and 2.4
PUMP_FLOWRATE_OUT_T3 = 2.40
PUMP_FLOWRATE_OUT_T4 = 2.35
PUMP_FLOWRATE_IN_T51 = 2.10
PUMP_FLOWRATE_IN_T52 = 0.25
PUMP_FLOWRATE_BACKWASH = 2.00
# periods in msec
# R/W = Read or Write
T_PLC_R = 100E-3
T_PLC_W = 100E-3

T_PP_R = 200E-3
T_PP_W = 200E-3
T_HMI_R = 100E-3

# ImageTk
DISPLAYED_SAMPLES = 14

# Control logic thresholds
LIT_101_MM = {  # raw water tank mm
    'LL': 250.0,
    'L': 500.0,
    'H': 800.0,
    'HH': 1200.0,
}
LIT_101_M = {  # raw water tank m
    'LL': 0.250,
    'L': 0.500,
    'H': 0.800,
    'HH': 1.200,
}

LIT_301_MM = {  # ultrafiltration tank mm
    'LL': 250.0,
    'L': 800.0,
    'H': 1000.0,
    'HH': 1200.0,
}
LIT_301_M = {  # ultrafiltration tank m
    'LL': 0.250,
    'L': 0.800,
    'H': 1.000,
    'HH': 1.200,
}
LIT_401_MM = {  # ultrafiltration tank mm
    'LL': 250.0,
    'L': 800.0,
    'H': 1000.0,
    'HH': 1200.0,
}
LIT_401_M = {  # ultrafiltration tank m
    'LL': 0.250,
    'L': 0.800,
    'H': 1.000,
    'HH': 1.200,
}
LIT_501_MM = {  # ultrafiltration tank mm
    'LL': 250.0,
    'L': 800.0,
    'H': 3000.0,
    'HH': 4200.0,
}
LIT_501_M = {  # ultrafiltration tank m
    'LL': 0.250,
    'L': 0.800,
    'H': 3.000,
    'HH': 4.200,
}

LIT_502_MM = {  # ultrafiltration tank mm
    'LL': 250.0,
    'L': 800.0,
    'H': 1000.0,
    'HH': 1200.0,
}
LIT_502_M = {  # ultrafiltration tank m
    'LL': 0.250,
    'L': 0.800,
    'H': 1.000,
    'HH': 1.200,
}
TANK_HEIGHT = 1.600  # m

PLC_PERIOD_SEC = 0.40  # plc update rate in seconds
PLC_PERIOD_HOURS = PLC_PERIOD_SEC / 3600.0
PLC_SAMPLES = 5000

PP_RESCALING_HOURS = 100
PP_PERIOD_SEC = 0.20  # physical process update rate in seconds
PP_PERIOD_HOURS = (PP_PERIOD_SEC / 3600.0) * PP_RESCALING_HOURS
PP_SAMPLES = int(PLC_PERIOD_SEC / PP_PERIOD_SEC) * PLC_SAMPLES

RWT_INIT_LEVEL = 0.500  # l

# m^3 / h
FIT_201_THRESH = 1.00
# SPHINX_SWAT_TUTORIAL PROCESS UTILS)

# topo {{{1
IP = {
    'plc1': '192.168.1.10',
    'plc2': '192.168.1.20',
    'plc3': '192.168.1.30',
    'plc4': '192.168.1.40',
    'plc5': '192.168.1.50',
    'plc6': '192.168.1.60',
    'hmi': '192.168.1.70',
    'attacker': '192.168.1.77',
}

NETMASK = '/24'

MAC = {
    'plc1': '00:1D:9C:C7:B0:70',
    'plc2': '00:1D:9C:C8:BC:46',
    'plc3': '00:1D:9C:C8:BD:F2',
    'plc4': '00:1D:9C:C7:FA:2C',
    'plc5': '00:1D:9C:C8:BC:2F',
    'plc6': '00:1D:9C:C7:FA:2D',
    'hmi': '00:1D:9C:C8:BC:70',
    'attacker': 'AA:AA:AA:AA:AA:AA',
}


# others
# TODO
HMI_DATA = {
    'TODO': 'TODO',
}

PLC1_DATA = {
    'TODO': 'TODO',
}
# TODO
PLC2_DATA = {
    'TODO': 'TODO',
}
# TODO
PLC3_DATA = {
    'TODO': 'TODO',
}

PLC4_DATA = {
    'TODO': 'TODO',
}
PLC5_DATA = {
    'TODO': 'TODO',
}
PLC6_DATA = {
    'TODO': 'TODO',
}


# SPHINX_SWAT_TUTORIAL PLC1 UTILS(
HMI_ADDR = IP['hmi']
HMI_PROTOCOL = {
    'name': 'enip',
    'mode': 0,
    'server': None
}

PLC1_ADDR = IP['plc1']
PLC1_TAGS = (
    ('FIT101', 1, 'REAL'),
    ('MV101', 1, 'INT'),
    ('LIT101', 1, 'REAL'),
    ('P101', 1, 'INT'),
    # interlocks does NOT go to the statedb
    ('FIT201', 1, 'REAL'),
    ('MV201', 1, 'INT'),
    ('LIT301', 1, 'REAL'),
)
PLC1_SERVER = {
    'address': PLC1_ADDR,
    'tags': PLC1_TAGS
}
PLC1_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC1_SERVER
}
# SPHINX_SWAT_TUTORIAL PLC1 UTILS)

PLC2_ADDR = IP['plc2']
PLC2_TAGS = (
    ('FIT201', 2, 'REAL'),
    ('MV201', 2, 'INT'),
    # no interlocks
)
PLC2_SERVER = {
    'address': PLC2_ADDR,
    'tags': PLC2_TAGS
}
PLC2_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC2_SERVER
}

PLC3_ADDR = IP['plc3']
PLC3_TAGS = (
    ('LIT301', 3, 'REAL'),
    ('FIT301', 3, 'REAL'),
    ('P301', 3, 'INT'),
    # no interlocks
)
PLC3_SERVER = {
    'address': PLC3_ADDR,
    'tags': PLC3_TAGS
}
PLC3_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC3_SERVER
}

PLC4_ADDR = IP['plc4']
PLC4_TAGS = (
    ('LIT401', 4, 'REAL'),
    ('FIT401', 4, 'REAL'),
    ('P401', 4, 'INT'),
    # no interlocks
)
PLC4_SERVER = {
    'address': PLC4_ADDR,
    'tags': PLC4_TAGS
}
PLC4_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC4_SERVER
}

PLC5_ADDR = IP['plc5']
PLC5_TAGS = (
    ('P501', 5, 'INT'),
    # no interlocks
)
PLC5_SERVER = {
    'address': PLC5_ADDR,
    'tags': PLC5_TAGS
}
PLC5_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC5_SERVER
}

PLC6_ADDR = IP['plc6']
PLC6_TAGS = (
    ('LIT501', 5, 'REAL'),
    ('LIT502', 5, 'REAL'),
    ('P602', 6, 'INT'),
    # no interlocks
)
PLC6_SERVER = {
    'address': PLC6_ADDR,
    'tags': PLC6_TAGS
}
PLC6_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC6_SERVER
}
# state {{{1
# SPHINX_SWAT_TUTORIAL STATE(
PATH = 'swat_db.sqlite'
NAME = 'swat'

STATE = {
    'name': NAME,
    'path': PATH
}
# SPHINX_SWAT_TUTORIAL STATE)

SCHEMA = """
CREATE TABLE swat (
    name              TEXT NOT NULL,
    pid               INTEGER NOT NULL,
    value             TEXT,
    PRIMARY KEY (name, pid)
);
"""

SCHEMA_INIT = """
    INSERT INTO swat VALUES ('FIT101',   1, '2.55');
    INSERT INTO swat VALUES ('MV101',    1, '0');
    INSERT INTO swat VALUES ('LIT101',   1, '0.500');
    INSERT INTO swat VALUES ('P101',     1, '1');

    INSERT INTO swat VALUES ('FIT201',   2, '2.45');
    INSERT INTO swat VALUES ('MV201',    2, '1');

    INSERT INTO swat VALUES ('LIT301',   3, '0.000');
    INSERT INTO swat VALUES ('FIT301',   3, '2.40');
    INSERT INTO swat VALUES ('P301',   3, '0');

    INSERT INTO swat VALUES ('LIT401',   4, '0.000');
    INSERT INTO swat VALUES ('FIT401',   4, '2.35');
    INSERT INTO swat VALUES ('P401',   4, '0');

    INSERT INTO swat VALUES ('P501',   5, '0');
    INSERT INTO swat VALUES ('FIT501',  5, '2.10');
    INSERT INTO swat VALUES ('FIT502',   5, '0.25');

    INSERT INTO swat VALUES ('LIT501',   5, '0.000');
    INSERT INTO swat VALUES ('LIT502',   5, '0.000');
    INSERT INTO swat VALUES ('P602',   6, '0');
    INSERT INTO swat VALUES ('FIT602',   6, '2.00');

"""