n, m = map(int, input().split())
tasks = [int(x) for x in input().split()]
intervals = [int(x) for x in input().split()]
tasks.sort(reverse=True)
intervals.sort(reverse=True)
j = 0
total = 0
for i in range(n):
    if tasks[i] <= intervals[j]:
        total += 1
        j += 1
    if j == m:
        break
print(total)