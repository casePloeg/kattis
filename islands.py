p = int(input())
for _ in range(p):
    line = list(map(int, input().split()))
    t = line.pop(0)
    nums = line
    total = 0
    for i in range(1, 11):
        # every number most be bigger than left boundary
        l = nums[i-1] 
        for j in range(i, 11):
            # maintain property that nums inbetween i and j
            # is greater than the numbers at i-1 and j+1
            r = nums[j+1] 
            valid = True
            for k in range(i, j+1):
                if nums[k] <= l or nums[k] <= r:
                    valid = False
                    break
            if valid:
                total += 1
    print(t, total)

