import sys


# get the number of test cases
t = int(sys.stdin.readline())
# iterate through the test cases
for i in range(0, t):
    # read info for the test case
    info = sys.stdin.readline().split()
    # convert elements to ints
    for j in range(0, len(info)):
        info[j] = int(info[j])
    # create a variable to keep track of the number of non native turtles
    imports = 0
    # the calculation should end when the zero in the list is found
    # create a counter for the day
    day = 0
    population = info[day]
    while(population != 0):
        # increment the day counter 
        day += 1
        new_population = info[day]
        max_native = population * 2
        if(max_native < new_population):
            imports += new_population - max_native
        population = new_population
    # output the lower bound of imports
    print(imports)
