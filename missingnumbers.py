n = int(input())

flag = False
recited = int(input())
cur = 1
i = 0

while i < n-1 or cur < recited:    
    if cur < recited:
        print(cur)
        flag = True
        cur += 1
    else:
        cur += 1
        recited = int(input())
        i += 1

if not flag:
    print("good job")

