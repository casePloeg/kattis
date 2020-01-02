class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        sign = [-1, 1][x > 0]
        res = str(x)[::-1] if sign == 1 else str(x)[1:][::-1]

        res = int(res) if sign == 1 else int(res) * -1
        if -2 ** 31 <= res < 2 ** 31:
            return res
        return 0

s = Solution()
print(s.reverse(
1534236469))