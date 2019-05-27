import os.path
import re
from collections import namedtuple

def extract_data_from_file(filename, regex):
    data = []
    data_struct = namedtuple("Struct", "Name Max Min")
    with open(os.path.join(os.path.dirname(__file__), filename), "r") as f:
        lines = f.readlines()

        for line in lines[:len(lines)-1]:
            match = re.search(regex, line)
            if (match):
                entry = data_struct(str(match.group(1)), int(match.group(2)), int(match.group(3)))
                data.append(entry)

    return data

def min_difference(data):
    min_difference = data[0].Max - data[0].Min
    min_team = data[0].Name
    for entry in data[1:]:
        difference = entry.Max - entry.Min
        
        if difference < min_difference:
            min_difference = difference
            min_team = entry.Name

    return min_team