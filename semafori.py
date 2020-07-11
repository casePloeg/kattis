n, l = map(int, input().split())
lights = [list(map(int, input().split())) for _ in range(n)]
time = 0
pos = 0
while pos < l:
    wait = False
    for light in lights:
        d, r, g = light
        if pos == d and time % (r+g) < r:
            wait = True
    if not wait:
        pos += 1
    time += 1
print(time)
    
