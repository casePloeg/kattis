k = int(input())
size = 0
breaks = 0
parts = []
while k > 0:
    size += 1
    parts.append(k%2)
    k //= 2
parts = parts[::-1]
for i in range(size):
    if parts[i] == 1:
        breaks = i
if breaks == 0:
    size -= 1
else:
    breaks += 1
print(2 ** size, breaks)
