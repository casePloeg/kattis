import sys


# create a list for the hours of the day
hours = []
for i in range(0, 24):
    hours.append(i)

# get the input line
line = sys.stdin.readline()
# split the input line into a list
line_list = line.split()

# convert the elements of the list to integers
given_hour = int(line_list[0])
given_min = int(line_list[1])

# if the minutes is less than 45
if(given_min < 45):
    # set the alarm time to be (given hour - 1, given min + (60 - 45)
    new_hour = hours[(given_hour - 1)]
    new_min = (given_min + 15)
# else
else:
    # set the alarm time to be: (given hour, given min - 45)
    new_hour = given_hour
    new_min = (given_min - 45)

# output the calculated alarm time
print(str(new_hour) + ' ' + str(new_min))