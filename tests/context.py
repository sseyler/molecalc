import configparser
import logging
import pathlib
import sys

try:
    import molecalc
    import molecalc_lib
except ImportError:
    parent = str(pathlib.Path(__file__).absolute().parent.parent)
    sys.path.insert(0, parent)
    import molecalc
    import molecalc_lib

import ppqm

# TODO Should be handled by pytest
SCR = ".test/"
RESOURCES = pathlib.Path("tests/resources/chemistry")


def ini_settings(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    return config


# Init enviroment
CONFIG = ini_settings("development.ini")
pathlib.Path(SCR).mkdir(parents=True, exist_ok=True)

molcalc = molecalc
molcalc_lib = molecalc_lib
ppqm = ppqm

logging.basicConfig(level=logging.DEBUG)
