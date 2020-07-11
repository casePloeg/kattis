c, p = map(int, input().split())
columns = list(map(int, input().split()))
if p == 1:
    total = 0
    for i in range(c-3):
        if columns[i] == columns[i+1] == columns[i+2] == columns[i+3]:
            total += 1
    total += c
    print(total)
elif p == 2:
    total = 0
    for i in range(c-1):
        if columns[i] == columns[i+1]:
            total += 1
    print(total)
elif p == 3:
    total = 0
    for i in range(c-1):
        if columns[i] == columns[i+1]+1:
            total += 1
    for i in range(c-2):
        if columns[i] == columns[i+1] == columns[i+2]-1:
            total += 1
    print(total)
elif p == 4:
    total = 0
    for i in range(c-1):
        if columns[i] == columns[i+1]-1:
            total += 1
    for i in range(c-2):
        if columns[i]-1 == columns[i+1] == columns[i+2]:
            total += 1
    print(total)
elif p == 5:
    total = 0
    for i in range(c-2):
        if columns[i] == columns[i+1] == columns[i+2]:
            total += 1
        if columns[i]-1 == columns[i+1] == columns[i+2]-1:
            total += 1
    for i in range(c-1):
        if columns[i] == columns[i+1]-1:
            total += 1
        if columns[i] == columns[i+1]+1:
            total += 1
    print(total)
elif p == 6:
    total = 0
    for i in range(c-1):
        if columns[i] == columns[i+1]:
            total += 1
        if columns[i]-2 == columns[i+1]:
            total += 1
    for i in range(c-2):
        if columns[i] == columns[i+1] == columns[i+2]:
            total += 1
        if columns[i]+1 == columns[i+1] == columns[i+2]: 
            total += 1
    print(total)

elif p == 7:
    total = 0
    for i in range(c-1):
        if columns[i] == columns[i+1]:
            total += 1
        if columns[i]+2 == columns[i+1]:
            total += 1
    for i in range(c-2):
        if columns[i] == columns[i+1] == columns[i+2]:
            total += 1
        if columns[i] == columns[i+1] == columns[i+2]+1: 
            total += 1
    print(total)

