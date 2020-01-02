from sys import stdin

for line in stdin:
    n, l, w = map(int, line.split())
    circles = []
    for i in range(n):
        data = input().split()
        x, r = int(data[0]), int(data[1])
        # transform into interval
        if r > w/2:
            interval = [max(0, x - (r**2 - (w/2)**2)**(1/2)), max(0, x + (r**2 - (w/2)**2)**(1/2))]
        else:
            interval = [-1, -1]
        circles.append(interval)
    circles.sort()
    min_num = 0
    cur_x = 0
    i = 0
    while i < n and circles[i][0] <= cur_x and cur_x < l:
        next_x = 0
        while i < n and circles[i][0] <= cur_x:
            next_x = max(next_x, circles[i][1])
            i += 1
        if next_x > cur_x:
            cur_x = next_x
            min_num += 1

    if cur_x >= l:
        print(min_num)
    else:
        print(-1)

