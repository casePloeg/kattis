class Solution:
    def subsets(self, nums):
        def combinations(nums, length):
            if length > 0:
                res = []
                for i, n in enumerate(nums):
                    combs = combinations(nums[:i] + nums[i + 1:], length - 1)
                    for c in combs:
                        res.append([n] + c)
            else:
                res = [[]]
            return res

        subsets = []
        for i in range(len(nums) + 1):
            subsets += combinations(nums, i)
        return subsets


s = Solution()
print(s.subsets([1,2,3,4]))