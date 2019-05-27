import common

# It can be sorted and then just return first
def minimum_difference():
    data = common.extract_data_from_file("football.dat", r"\d\. (\w+)\s+\d+\s+\d+\s+\d+\s+\d+\s+([\d]+)  -  ([\d]+)\s+")

    return common.min_difference(data)

