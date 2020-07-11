n = int(input())
dirty = list(map(int, input().split()))
phases = 0
count = 0
d_i = 0
for i in range(366):
    for d in dirty[d_i:]:
        if d <= i:
            count += 1
    if count >= 20:
        phases += 1
        for j, d in enumerate(dirty):
            if d <= i:
                d_i = j + 1
        count = 0
if count > 0:
    phases += 1

print(phases)
