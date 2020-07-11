import itertools


def leap(year):
    if year % 400 == 0:
        return 1
    elif year % 100 == 0:
        return 0
    elif year % 4 == 0:
        return 1
    return 0


t = int(input())
for _ in range(t):
    line = input()
    nums = []
    for c in line:
        if c.isnumeric():
            nums.append(int(c))
    options = itertools.permutations(nums)
    valid = set()
    for o in options:
        d1 = o[0]
        d2 = o[1]
        m1 = o[2]
        m2 = o[3]
        y1 = o[4]
        y2 = o[5]
        y3 = o[6]
        y4 = o[7]
        day = d1 * 10 + d2
        month = m1 * 10 + m2
        month -= 1
        year = y1 * 1000 + y2 * 100 + y3 * 10 + y4
        v = False
        if year >= 2000 and -1 < month <= 11 and 0 < day:
            if month == 0 and day <= 31:
                v = True
            elif month == 1 and day <= (28 + (leap(year))):
                v = True
            elif month == 2 and day <= 31:
                v = True
            elif month == 3 and day <= 30:
                v = True
            elif month == 4 and day <= 31:
                v = True
            elif month == 5 and day <= 30:
                v = True
            elif month == 6 and day <= 31:
                v = True
            elif month == 7 and day <= 31:
                v = True
            elif month == 8 and day <= 30:
                v = True
            elif month == 9 and day <= 31:
                v = True
            elif month == 10 and day <= 30:
                v = True
            elif month == 11 and day <= 31:
                v = True
        month += 1
        if v:
            valid.add((day, month, year))
    if len(valid) > 0:
        valid = list(valid)
        valid.sort(key=lambda x: (x[2], x[1], x[0]))
        print(len(valid), '{:02d}'.format(valid[0][0]), '{:02d}'.format(valid[0][1]), valid[0][2])
    else:
        print(0)
