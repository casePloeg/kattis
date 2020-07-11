from collections import deque


# model as a multi source path finding problem
# transitions are the angles known, searching for
# path to current angle

# run bfs until run out of new angles to check
# max 360 angles so run time is constant
n, k = map(int, input().split())
m = list(map(int, input().split()))
s = list(map(int, input().split()))
for a in s:
    q = deque()
    for u in m:
        q.append(u)
    valid = False
    visited = set()
    while len(q) > 0:
        u = q.popleft()
        if u == a:
            valid = True
            break
        for v in m:
            u1 = (u - v) % 360
            u2 = (u + v) % 360
            if u1 not in visited:
                q.append(u1)
                visited.add(u1)
            if u2 not in visited:
                q.append(u2)
                visited.add(u2)

    if valid:
        print('YES')
    else:
        print('NO')
