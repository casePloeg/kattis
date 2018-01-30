import sys


# iterate through the sets until the end of the file is reached
n = int(sys.stdin.readline())
# create a counter for the number of sets
counter = 1
while(n != 0):
    # create a list for the set of names
    name_list = []
    # iterate through the names in the list
    for i in range(0, n):
        # read the name
        name = sys.stdin.readline().replace('\n','')
        # every other name should go to the front, the other to the back
        name_list.append(name)
    # create a list of the ordered names
    ordered_names = []
    # create a counter to keep track of whether the name should go at the front
    # or back
    if(n % 2 == 0):
        front = False
    else:
        front = True
    for j in range(n-1, -1, -1):
        if(front):
            ordered_names = [name_list[j]] + ordered_names
            front = False
        else:
            ordered_names.append(name_list[j])     
            front = True
    # put the set indentification at the start of the list
    ordered_names = [('SET ' + str(counter))] + ordered_names
    # increment the counter
    counter += 1
    # move to next set 
    n = int(sys.stdin.readline())
    # output the list where each element is on a seperate line
    for i in ordered_names:
        print(i)