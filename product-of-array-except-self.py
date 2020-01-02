class Solution:
    def productExceptSelf(self, nums):
        pre_product = [1]
        post_product = [1]
        prev = 1
        post = 1
        for n in nums:
            pre_product.append(n * prev)
            prev = n * prev
        for n in reversed(nums):
            post_product.append(n * post)
            post = n * post
        res = [None for _ in range(len(nums))]
        for i in range(len(nums)):
            res[i] = pre_product[i] * post_product[-2-i]
        return res


s = Solution()
print(s.productExceptSelf([1,2,3,4]))