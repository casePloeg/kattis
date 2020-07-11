diff = int(input())
m = 0
w = 0
q = list(input())
best = len(q)

while m+w < best: 
    first = q[0]
    nxt_m = m
    nxt_w = w
    if first == 'M':
        nxt_m += 1
    else:
        nxt_w += 1

    if abs(nxt_m - nxt_w) > diff and len(q) > 1:
        sec = q[1]
        if sec == first:
            break
        elif sec == 'M':
            nxt_m = m + 1
            nxt_w = w
        else:
            nxt_m = m
            nxt_w = w + 1
        q.pop(1)
    elif abs(nxt_m - nxt_w) > diff:
        break
    else:
        q.pop(0)
    m, w = nxt_m, nxt_w

print(m+w)

