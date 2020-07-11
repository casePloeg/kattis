info = input()
while info != '0':
    k, m = map(int, info.split())
    valid = True
    selections = input().split()
    for i in range(m):
        cat = input().split()
        c = int(cat[0])
        r = int(cat[1])
        taken = 0
        for j in range(2,len(cat)):
            if cat[j] in selections:
                taken += 1
        if taken < r: 
            valid = False
    if valid:
        print('yes')
    else:
        print('no')
    info = input()
