class Solution:
    def findDuplicate(self, nums):
        walker = 0
        runner = 0
        while walker == runner or nums[walker] != nums[runner]:
            walker = nums[walker]
            runner = nums[nums[runner]]
        return nums[walker]

s = Solution()
print(s.findDuplicate([1,3,4,2,2]))