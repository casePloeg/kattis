import sys


# create a variable that represents whether the loop
# should continue to run or not
run = True
# while the end of the final has not been reached
while(run):
    # read the line containing the number n which indicates the 
    # number of calculations needed within the set
    n = int(sys.stdin.readline())
    # if -1 shows up end the loop
    if( n == -1):
        run = False
    else:
        # create a variable for the number of miles driven
        miles = 0
        # create a variable that saves the past time
        past_time = 0             
        # loop through the data for the calculations
        for i in range(0, n):  
            # read the data for the calculation
            miles_data = sys.stdin.readline()

            # convert the data to a list
            miles_data = miles_data.split()

            # convert the values to integers
            miles_data[0] = int(miles_data[0])
            miles_data[1] = int(miles_data[1])

            # create a variable for the current time section
            time_section = miles_data[1] - past_time
            
            # update the past time
            past_time = miles_data[1]

            # calculate the number of miles driven for
            # this part of the data set (current time * speed)
            miles_section = (time_section * miles_data[0])

            # increment the miles driven
            miles += miles_section

        # output the miles driven for the data set
        print(str(miles) + " miles")