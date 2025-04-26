data_path = "Data/ctabus.csv"

# A tuple 1
# A dictionary 2


# A class 3
class Row3:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


# A named tuple 4
from collections import namedtuple

Row4 = namedtuple("Row", ["route", "date", "daytype", "rides"])


# A class with __slots__ 5
class Row5:
    __slots__ = ["route", "date", "daytype", "rides"]

    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


import csv


def read_rides(dat_type, data_path):
    records = []
    with open(data_path) as f:
        rows = csv.reader(f)
        headings = next(rows)  # headings, useful for defining let's say keys in dict
        for row in rows:
            route, date, daytype = row[0], row[1], row[2]
            rides = int(row[3])

            if dat_type == 1:
                records.append((route, date, daytype, rides))

            if dat_type == 2:
                row = {
                    "route": route,
                    "date": date,
                    "daytype": daytype,
                    "rides": rides,
                }
                records.append(row)

            if dat_type == 3:
                row = Row3(route, date, daytype, rides)
                records.append(row)

            if dat_type == 4:
                row = Row4(route, date, daytype, rides)
                records.append(row)

            if dat_type == 5:
                row = Row5(route, date, daytype, rides)
                records.append(row)

        return records


if __name__ == "__main__":
    import tracemalloc

    memory_data = []

    for i in range(1, 6):
        tracemalloc.start()
        rows = read_rides(i, data_path)
        if i == 1:
            data_type = "tuple"
        if i == 2:
            data_type = "dict"
        if i == 3:
            data_type = "plain_class"
        if i == 4:
            data_type = "named_tuple"
        if i == 5:
            data_type = "class_with_slots"

        print(
            "Memory Use for %s: Current %d, Peak %d"
            % (data_type, *tracemalloc.get_traced_memory())
        )
        memory_data.append(tracemalloc.get_traced_memory())
        tracemalloc.stop()

    print(memory_data)

    
#######################################################
####### RESULTS -> Slots are the most efficient########
#######################################################
# Memory Use for tuple: Current 114729046, Peak 114763633
# Memory Use for dict: Current 179416462, Peak 179451029
# Memory Use for plain_class: Current 128593694, Peak 128628189
# Memory Use for named_tuple: Current 119349998, Peak 119384485
# Memory Use for class_with_slots: Current 110108918, Peak 110143389
# [(114729038, 114763633), (179416454, 179451029), (128593686, 128628189), (119349990, 119384485), (110108910, 110143389)]
# >>> for i in range(5):
# ...     if min_curr > memory_data[i][0] and min_peak > memory_data[i][1]:
# ...              min_curr, min_peak = memory_data[i]
# ...
# >>> print(min_curr, min_peak)
# 110108910 110143389
# >>> print(f"{min_curr:,}", f"{min_peak:,}")
# 110,108,910 110,143,389
# >>>
