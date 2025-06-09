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
    'plc1': '192.168.1.1',
    'plc2': '192.168.1.2',
    'plc3': '192.168.1.3',
    'plc4': '192.168.1.4',
    'plc5': '192.168.1.5',
    'plc6': '192.168.1.6',
    'plc7': '192.168.1.7',
    'plc8': '192.168.1.8',
    'plc9': '192.168.1.9',
    'plc10': '192.168.1.10',
    'plc11': '192.168.1.11',
    'plc12': '192.168.1.12',
    'plc13': '192.168.1.13',
    'plc14': '192.168.1.14',
    'plc15': '192.168.1.15',
    'plc16': '192.168.1.16',
    'plc17': '192.168.1.17',
    'plc18': '192.168.1.18',
    'plc19': '192.168.1.19',
    'plc20': '192.168.1.20',
    'plc21': '192.168.1.21',
    'plc22': '192.168.1.22',
    'plc23': '192.168.1.23',
    'plc24': '192.168.1.24',
    'plc25': '192.168.1.25',
    'plc26': '192.168.1.26',
    'plc27': '192.168.1.27',
    'plc28': '192.168.1.28',
    'plc29': '192.168.1.29',
    'plc30': '192.168.1.30',
    'plc31': '192.168.1.31',
    'plc32': '192.168.1.32',
    'plc33': '192.168.1.33',
    'plc34': '192.168.1.34',
    'plc35': '192.168.1.35',
    'plc36': '192.168.1.36',
    'hmi': '192.168.1.70',
    'attacker': '192.168.1.77',
}

NETMASK = '/24'

MAC = {
    'plc1': '00:1D:9C:C7:B0:10',
    'plc2': '00:1D:9C:C8:BC:20',
    'plc3': '00:1D:9C:C8:BD:30',
    'plc4': '00:1D:9C:C7:FA:40',
    'plc5': '00:1D:9C:C8:BC:50',
    'plc6': '00:1D:9C:C7:FA:60',
    'plc7': '00:2D:9C:C7:B0:10',
    'plc8': '00:2D:9C:C8:BC:20',
    'plc9': '00:2D:9C:C8:BD:30',
    'plc10': '00:2D:9C:C7:FA:40',
    'plc11': '00:2D:9C:C8:BC:50',
    'plc12': '00:2D:9C:C7:FA:60',
    'plc13': '00:3D:9C:C7:B0:10',
    'plc14': '00:3D:9C:C8:BC:20',
    'plc15': '00:3D:9C:C8:BD:30',
    'plc16': '00:3D:9C:C7:FA:40',
    'plc17': '00:3D:9C:C8:BC:50',
    'plc18': '00:3D:9C:C7:FA:60',
    'plc19': '00:4D:9C:C7:B0:10',
    'plc20': '00:4D:9C:C8:BC:20',
    'plc21': '00:4D:9C:C8:BD:30',
    'plc22': '00:4D:9C:C7:FA:40',
    'plc23': '00:4D:9C:C8:BC:50',
    'plc24': '00:4D:9C:C7:FA:60',
    'plc25': '00:5D:9C:C7:B0:10',
    'plc26': '00:5D:9C:C8:BC:20',
    'plc27': '00:5D:9C:C8:BD:30',
    'plc28': '00:5D:9C:C7:FA:40',
    'plc29': '00:5D:9C:C8:BC:50',
    'plc30': '00:5D:9C:C7:FA:60',
    'plc31': '00:6D:9C:C7:B0:10',
    'plc32': '00:6D:9C:C8:BC:20',
    'plc33': '00:6D:9C:C8:BD:30',
    'plc34': '00:6D:9C:C7:FA:40',
    'plc35': '00:6D:9C:C8:BC:50',
    'plc36': '00:6D:9C:C7:FA:60',
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

PLC_TAGS = (
    ('LIT101', 1, 'REAL'),
    ('MV101', 1, 'INT')
)

PLC1_ADDR = IP['plc1']
PLC1_TAGS = (
    ('FIT101', 1, 'REAL'),
    ('MV101', 1, 'INT'),
    ('LIT101', 1, 'REAL'),
    ('P101', 1, 'INT'),
    # interlocks does NOT go to the statedb
    ('FIT201', 1, 'REAL'),
    ('MV201', 1, 'INT'),
    ('LIT301', 1, 'REAL')
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

PLC7_SERVER = {
    'address': IP['plc7'],
    'tags': PLC_TAGS
}
PLC7_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC7_SERVER
}

PLC8_SERVER = {
    'address': IP['plc8'],
    'tags': PLC_TAGS
}
PLC8_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC8_SERVER
}

PLC9_SERVER = {
    'address': IP['plc9'],
    'tags': PLC_TAGS
}
PLC9_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC9_SERVER
}

PLC10_SERVER = {
    'address': IP['plc10'],
    'tags': PLC_TAGS
}
PLC10_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC10_SERVER
}

PLC11_SERVER = {
    'address': IP['plc11'],
    'tags': PLC_TAGS
}
PLC11_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC11_SERVER
}

PLC12_SERVER = {
    'address': IP['plc12'],
    'tags': PLC_TAGS
}
PLC12_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC12_SERVER
}

PLC13_SERVER = {
    'address': IP['plc13'],
    'tags': PLC_TAGS
}
PLC13_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC13_SERVER
}

PLC14_SERVER = {
    'address': IP['plc14'],
    'tags': PLC_TAGS
}
PLC14_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC14_SERVER
}

PLC15_SERVER = {
    'address': IP['plc15'],
    'tags': PLC_TAGS
}
PLC15_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC15_SERVER
}

PLC16_SERVER = {
    'address': IP['plc16'],
    'tags': PLC_TAGS
}
PLC16_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC16_SERVER
}

PLC17_SERVER = {
    'address': IP['plc17'],
    'tags': PLC_TAGS
}
PLC17_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC17_SERVER
}

PLC18_SERVER = {
    'address': IP['plc18'],
    'tags': PLC_TAGS
}
PLC18_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC18_SERVER
}

PLC19_SERVER = {
    'address': IP['plc19'],
    'tags': PLC_TAGS
}
PLC19_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC19_SERVER
}

PLC20_SERVER = {
    'address': IP['plc20'],
    'tags': PLC_TAGS
}
PLC20_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC20_SERVER
}

PLC21_SERVER = {
    'address': IP['plc21'],
    'tags': PLC_TAGS
}
PLC21_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC21_SERVER
}

PLC22_SERVER = {
    'address': IP['plc22'],
    'tags': PLC_TAGS
}
PLC22_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC22_SERVER
}

PLC23_SERVER = {
    'address': IP['plc23'],
    'tags': PLC_TAGS
}
PLC23_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC23_SERVER
}

PLC24_SERVER = {
    'address': IP['plc24'],
    'tags': PLC_TAGS
}
PLC24_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC24_SERVER
}

PLC25_SERVER = {
    'address': IP['plc25'],
    'tags': PLC_TAGS
}
PLC25_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC25_SERVER
}

PLC26_SERVER = {
    'address': IP['plc26'],
    'tags': PLC_TAGS
}
PLC26_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC26_SERVER
}

PLC27_SERVER = {
    'address': IP['plc27'],
    'tags': PLC_TAGS
}
PLC27_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC27_SERVER
}

PLC28_SERVER = {
    'address': IP['plc28'],
    'tags': PLC_TAGS
}
PLC28_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC28_SERVER
}

PLC29_SERVER = {
    'address': IP['plc29'],
    'tags': PLC_TAGS
}
PLC29_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC29_SERVER
}
PLC30_SERVER = {
    'address': IP['plc30'],
    'tags': PLC_TAGS
}
PLC30_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC30_SERVER
}

PLC31_SERVER = {
    'address': IP['plc31'],
    'tags': PLC_TAGS
}
PLC31_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC31_SERVER
}

PLC32_SERVER = {
    'address': IP['plc32'],
    'tags': PLC_TAGS
}
PLC32_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC32_SERVER
}
PLC33_SERVER = {
    'address': IP['plc33'],
    'tags': PLC_TAGS
}
PLC33_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC33_SERVER
}
PLC34_SERVER = {
    'address': IP['plc34'],
    'tags': PLC_TAGS
}
PLC34_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC34_SERVER
}
PLC35_SERVER = {
    'address': IP['plc35'],
    'tags': PLC_TAGS
}
PLC35_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC35_SERVER
}
PLC36_SERVER = {
    'address': IP['plc36'],
    'tags': PLC_TAGS
}
PLC36_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC36_SERVER
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