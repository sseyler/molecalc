import configparser
import pathlib
import sys

try:
    import molcalc
except ImportError:
    parent = str(pathlib.Path(__file__).absolute().parent.parent)
    sys.path.insert(0, parent)
    import molcalc

import molcalc_lib
import ppqm

# TODO Should be handled by pytest
SCR = ".test/"


def ini_settings(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    return config


# Init enviroment
CONFIG = ini_settings("development.ini")
pathlib.Path(SCR).mkdir(parents=True, exist_ok=True)

molcalc = molcalc
molcalc_lib = molcalc_lib
ppqm = ppqm
