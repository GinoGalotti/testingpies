import os.path
import re
from collections import namedtuple

class FootballData:
    path = "football.dat"
    FootballStruct = namedtuple("FootballStruct", "Team For Against")

    def read_data(self):
        data = []
        regex = r"\d\. (\w+)\s+\d+\s+\d+\s+\d+\s+\d+\s+([\d]+)  -  ([\d]+)\s+"
        with open(os.path.join(os.path.dirname(__file__), self.path), "r") as f:
            lines = f.readlines()

            for line in lines[1:len(lines)-1]: # Because the first 2 lines aren't useful, and the last one is an average

                print("line is " + line)

                match = re.search(regex, line)
                if (match):
                    difference = self.FootballStruct(str(match.group(1)), int(match.group(2)), int(match.group(3)))
                    data.append(difference)

        return data

    def minimum_difference(self):
        data = self.read_data()

        min_difference = data[0].For - data[0].Against
        min_team = data[0].Team
        for entry in data[1:]:
            difference = entry.For - entry.Against
            
            if difference < min_difference:
                min_difference = difference
                min_team = entry.Team

        return min_team


    