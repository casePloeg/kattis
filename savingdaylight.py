import sys

for line in sys.stdin:
    month, day, year, sun_rise, sun_set = line.split()
    hr, mr = map(int, sun_rise.split(':'))
    hs, ms = map(int, sun_set.split(':'))
    dh = hs - hr
    dm = ms - mr
    if dm < 0:
        dm += 60
        dh -= 1
    print(month, day, year, dh, 'hours', dm, 'minutes')

