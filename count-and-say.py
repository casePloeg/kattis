class Solution:
    def sequence(self, seq):
        res = ''
        i = 0
        cur = seq[0]
        count = 0
        while i < len(seq):
            if cur != seq[i]:
                res += str(count) + str(cur)
                count = 1
                cur = seq[i]
            else:
                count += 1
            i += 1
        res += str(count) + str(cur)
        return res

    def countAndSay(self, n: int) -> str:
        seq = '1'
        for i in range(n - 1):
            seq = self.sequence(seq)
        return seq


s = Solution()
print(s.countAndSay(int(input())))