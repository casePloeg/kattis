# giving for PARTION (np complete problem)
# input bounds are small so runs okay
# to generate combinations use bitmask (gray code)
# check all combinations and look for a sum we've already
# seen stored in a dictionary
t = int(input())
for _ in range(t):
    print('Case #', _+1, ':', sep='')
    nums = list(map(int, input().split()))
    nums = nums[1:]
    flag = False
    sums = dict()
    i = 0
    while i < (2 ** 20 - 1):
        s = 0
        subset = []
        for j in range(20):
            if (i&(1<<j)):
                s += nums[j]
                subset.append(nums[j])

        if s in sums:
            print(' '.join([str(x) for x in subset]))
            print(' '.join([str(x) for x in sums[s]]))
            flag = True
            break
        else:
            sums[s] = subset
        i += 1

    if not flag:
        print('Impossible')


    
