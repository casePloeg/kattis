import sys

t = 1
for line in sys.stdin:
    line = line.strip()
    if line == 'END':
        break
    line = line[1:-1]
    px = line.split('*')
    even = True 
    for i in range(1, len(px)):
        if len(px[i]) != len(px[i-1]):
            even = False
            break
    if even:
        print(t, 'EVEN')
    else:
        print(t, 'NOT EVEN')
    t += 1

