n = int(input())
for _ in range(n):
    seq = list(map(int,input().split()))
    m = seq.pop(0)
    dif = seq[1] - seq[0]
    valid = True
    for i in range(1, m):
        d = seq[i] - seq[i-1]
        if d != dif:
            valid = False
            break
    if valid:
        print('arithmetic')
    else:
        seq.sort()
        dif = seq[1] - seq[0]
        valid = True
        for i in range(1, m):
            d = seq[i] - seq[i-1]
            if d != dif:
                valid = False
                break
        if valid:
            print('permuted arithmetic')
        else:
            print('non-arithmetic')

