import sys


# get the day and month
info = sys.stdin.readline().split()
# minus 1 to account for 0 indexing (laziness)
day = int(info[0]) - 1
month = int(info[1]) - 1
# the first day of the year is a thrusday
# create a dictionary that maps numbers 0-6 to a day
days = {0: 'Thursday', 1: 'Friday', 2: 'Saturday', 3: 'Sunday', 4: 'Monday',
        5: 'Tuesday', 6: 'Wednesday'}
# create dictionary that maps each month to the number of days in that month
months = {0: 31, 1: 28, 2: 31, 3: 30, 4: 31, 5: 30, 6: 31, 7: 31, 8: 30, 9: 31,
          10: 30, 11: 31}
# calculate the number of days have past
num_days = 0
for i in range(0, month):
    num_days += months[i]
num_days += day
# evaluate which day of the week it is
day_of_week = days[num_days % 7]
# output the day of the week
print(day_of_week)
