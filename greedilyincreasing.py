input()
nums = [int(x) for x in input().split()]
seq = []
seq.append(nums[0])
for i in range(len(nums)):
    if nums[i] > seq[-1]:
        seq.append(nums[i])

print(len(seq), ' '.join([str(x) for x in seq]))