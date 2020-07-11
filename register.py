vals = list(map(int, input().split()))
sizes = [2, 3, 5, 7, 11, 13, 17, 19]
n = 0
a = 0
for i, v in enumerate(vals):
    partial = v
    for j, s in enumerate(sizes):
        if j < i:
            partial *= s
    a += partial
print(9699689 - a)
