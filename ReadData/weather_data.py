import os.path
import re
from collections import namedtuple

import common

def minimum_difference():
    data = common.extract_data_from_file("weather.dat", r"\s+([\d]+)\*?\s+([\d]+)\*?\s+([\d]+)\*?")

    return common.min_difference(data)