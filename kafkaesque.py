n = int(input())
cur = 0
prev = 100
total = 0
for i in range(n):
    cur = int(input())
    if cur < prev: 
        total += 1
    prev = cur
print(total)

