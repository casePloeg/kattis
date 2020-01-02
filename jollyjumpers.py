import sys
for line in sys.stdin:
    nums = [int(x) for x in line.split()]
    n = nums[0]
    # n - 1 elements in the array
    differences = [0 for i in range(n)]
    valid = True
    for i in range(1, n):
        difference = abs(nums[i] - nums[i+1])
        # pigeon hole principle
        if 0 < difference < n and differences[difference - 1] == 0:
            differences[difference-1] = 1
        else:
            valid = False
            break
    if valid:
        print('Jolly')
    else:
        print('Not jolly')