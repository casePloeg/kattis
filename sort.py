from collections import defaultdict


n, c = map(int, input().split())
nums = list(map(int, input().split()))
freq = defaultdict(int)
f_t_n = defaultdict(list)

f_t_n[0] = list(set(nums))
for num in nums:
    freq[num] += 1 
    f_t_n[freq[num]].append(num)
    f_t_n[freq[num]-1].pop(f_t_n[freq[num]-1].index(num))
res = []
for i in reversed(range(1001)):
    if len(f_t_n[i]) > 0:
        f_t_n[i].sort(key=lambda x: nums.index(x))
        for num in f_t_n[i]:
            res += [num for x in range(i)]
print(' '.join([str(x) for x in res]))
