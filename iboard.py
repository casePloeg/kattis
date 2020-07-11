import sys

for line in sys.stdin:
    line = line.strip()
    l = False
    r = False
    for c in line:
        n = ord(c)
        i = 0
        while n > 0:
            if n % 2 == 1:
                l = not l
            else:
                r = not r
            n //= 2
            i += 1
        while i < 7:
            r = not r 
            i += 1
    if l or r:
        print('trapped')
    else:
        print('free')
