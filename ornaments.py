import sys
import math

for line in sys.stdin:
    r, h, s = map(int, line.split())
    if r + h + s == 0:
        break
    string = 2 * (h**2 - r**2)**(1/2)
    string += ((360 - math.degrees(math.acos(r/h))*2)/360) * 2 * r * math.pi
    string += string * (s / 100)
    print('{:0.2f}'.format(string)) 

