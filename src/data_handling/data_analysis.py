import time 
before = time.time()

from multiple_read_rides import read_rides
from pprint import pprint
from collections import Counter
import re
import tracemalloc

rows = read_rides(2, 'Data/ctabus.csv')
pprint(rows[:10])

# 1) How many routes exist in Chicago
def count_routes() -> None:
    routes = set()

    for row in rows:
        routes.add(row['route'])

    return routes
    

# 2) How many people rode the number 22 bus on February 2, 2011? What about any route on any date of your choosing?

def count_rides(date, route):
    total = 0
    for row in rows:
        if row["date"] == date and row["route"] == route:
            total += row['rides']

    return total


# 3) What is the total number of rides taken on each bus route?
def total_rides():
    all_rides = Counter()

    for row in rows:
        all_rides[row['route']] += row['rides']

    return all_rides


# 4) What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?
def greates_increase():
    all_rides = Counter()

    for row in rows:
        if re.match(r".*/2001$", row['date']):
            all_rides[row['route']] -= row['rides']
        
        if re.match(r".*/2011$", row['date']):
            all_rides[row['route']] += row['rides']

    tracemalloc.start()
    max_5 = []
    for route, increase in all_rides.items():
        if len(max_5) < 5:
            max_5.append((route, increase))
            max_5.sort(key=lambda x: x[1], reverse=True)
        else:
            if increase > max_5[-1][1]:
                max_5[-1] = (route, increase)
                max_5.sort(key=lambda x: x[1], reverse=True)
    print(tracemalloc.get_traced_memory())
    tracemalloc.stop()

    
    return max_5

if __name__ == "__main__":
    print(time.time() - before)
    print(len(count_routes()))
    print(count_rides("02/02/2011", "22"))
    pprint(total_rides())
    print(greates_increase())
