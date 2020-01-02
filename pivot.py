import math

n = int(input())
nums = [int(_) for _ in input().split()]
is_pivot = [0 for i in range(n)]
highest = -math.inf
for i in range(n):
    if nums[i] > highest:
        is_pivot[i] = 1
        highest = nums[i]
lowest = math.inf
for i in range(n-1, -1, -1):
    if nums[i] < lowest:
        lowest = nums[i]
    else:
        is_pivot[i] = 0
print(sum(is_pivot))
