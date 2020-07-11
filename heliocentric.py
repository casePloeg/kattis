import sys

i = 1
for line in sys.stdin:
    e, m = map(int, line.split())
    days = 0
    while e % 365 != 0 or m % 687 != 0:
        e += 1
        m += 1
        e %= 365
        m %= 687
        days += 1
    print('Case ' + str(i) + ': ' + str(days))
    i += 1

