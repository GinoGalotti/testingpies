import os.path
import re
from collections import namedtuple

class WeatherData:
    path = "weather.dat"
    DataStruct = namedtuple("DataStruct", "Day Max Min")

    def read_data(self):
        data = []

        regex = r"\s+([\d]+)\*?\s+([\d]+)\*?\s+([\d]+)\*?"
        with open(os.path.join(os.path.dirname(__file__), self.path), "r") as f:
            lines = f.readlines()

            index = 0
            for line in lines[2:len(lines)-1]: # Because the first 2 lines aren't useful, and the last one is an average

                print("line is " + line)

                match = re.search(regex, line)

                day = self.DataStruct(int(match.group(1)), int(match.group(2)), int(match.group(3)))
                data.append(day)
                index += 1

        return data

    def minimum_spread(self):
        data = self.read_data()

        min_spread = data[0].Max - data[0].Min
        min_day = data[0].Day
        for day in data[1:]:
            spread = day.Max - day.Min
            
            if spread < min_spread:
                min_spread = spread
                min_day = day.Day

        return min_day