import math


def get_width(t, p):
    return math.ceil((9/16) * t * p)

def points(cw, cmax):
    return 8 + math.ceil((40 * (cw - 4)) / (cmax - 4))

width, n = map(int, input().split())
_ = 0
while width + n != 0:
    cur_w = 0
    h = 0
    occur = dict()
    cmax = 0
    for i in range(n):
        w, cw = input().split()
        cw = int(cw)
        cmax = max(cmax, cw)
        if (cw >= 5):
            occur[w] = cw

    delta_h = 0
    for w, cw in sorted(occur.items()):
        nxt = get_width(len(w), points(cw, cmax))
        if nxt + cur_w > width:
            h = h + delta_h
            delta_h = 0
            cur_w = nxt + 10
        else:
            cur_w += nxt + 10
        delta_h = max(delta_h, points(cw, cmax))
    h += delta_h

    print('CLOUD ', _+1, ': ', h, sep='')
    _ += 1
    width, n = map(int, input().split())
