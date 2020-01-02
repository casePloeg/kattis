import sys

for line in sys.stdin:
    if line.strip() == '0 0 0':
        break
    nums = [int(x) for x in line.split()]
    nums.sort()
    if nums[0]**2 + nums[1] ** 2 == nums[2] ** 2:
        print('right')
    else:
        print('wrong')