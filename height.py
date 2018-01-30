import sys


# get the number of data sets
p = int(sys.stdin.readline())
# iterate through the data sets
for i in range(0, p):
    # read the data set into a list
    info = sys.stdin.readline().split()
    # convert elements to integers
    for j in range(1, len(info)):
        info[j] = int(info[j])
    # create a list to hold the students as they are being sorted
    students = []
    
    # create a variable for the number of steps needed
    steps = 0
    # create a variable for the number of children out of place
    misplaced = 0
    # iterate through the students that need to be placed in the line
    for j in range(1, len(info)):
        # iterate through the students already in the line
        counter = 0
        is_placed = False
        while((counter < len(students)) and not is_placed):
            # if the current student is not the tallest in the line
            if((info[j] < students[counter]) or (counter == (len(students) - 1))):
                is_placed = True
                # put the student into the list so that the next tallest
                # student is directly behind them
                students.insert(counter, info[j])
                # all students behind the student that was just placed must
                # take a step back
                steps += (len(students[counter+1:]))
            counter += 1
    # output the data set number and the number of steps needed
    print(info[0] + ' ' + str(int(steps)))
