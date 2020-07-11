n = int(input())
while n != 0:
    xs = []
    ys = []
    for i in range(n):
        x, y = map(int, input().split())
        xs.append(x)
        ys.append(y)

    # add first element to the end of coord list
    # makes det calculation easier
    xs.append(xs[0])
    ys.append(ys[0])

    s = 0
    # calculate determinant of points
    for i in range(n):
        s -= xs[i+1] * ys[i]
        s += ys[i+1] * xs[i]
    s /= 2
    
    direction = ''
    # determinant is negative for CW
    if s < 0:
        direction = 'CW'
    else:
        direction = 'CCW'

    print(direction, '{:0.1f}'.format(abs(s)))
    n = int(input())
