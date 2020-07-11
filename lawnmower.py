nx, ny, w = map(float, input().split())
nx, ny = int(nx), int(ny)
while nx + ny + w != 0:
    end_to_end = list(map(float, input().split()))
    side_to_side = list(map(float, input().split()))
    end_to_end.sort()
    side_to_side.sort()
    cur = 0
    valid = True
    for s in end_to_end:
        if s - (w / 2) <= cur:
            cur = s + w / 2
        else:
            valid = False
            break
    valid = valid and cur >= 75
    if valid:
        cur = 0
        for s in side_to_side:
            if s - (w / 2) <= cur:
                cur = s + w / 2
            else:
                valid = False
                break
        valid = valid and cur >= 100
    if valid:
        print('YES')
    else:
        print('NO')

    nx, ny, w = map(float, input().split())
    nx, ny = int(nx), int(ny) 
