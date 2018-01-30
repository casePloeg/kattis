import sys


# get the number of test cases
test_cases = int(sys.stdin.readline())
# iterate through the test cases
for i in range(0, test_cases):
    # get the number of work trips
    work_trips = int(sys.stdin.readline())
    # create a set for the cities visted
    cities = set()
    # iterate through the trips
    for j in range(0, work_trips):
        # add the current city to the set
        city = sys.stdin.readline()
        cities.add(city)
    # output the length of the set (# of unique cities visted)
    num_cities = len(cities)
    print(num_cities)