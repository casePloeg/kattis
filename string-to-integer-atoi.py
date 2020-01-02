class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        num = ''
        i = 0
        start = False
        sign = 1
        while i < len(str):
            if not start:
                if str[i] == '-' or str[i].isnumeric():
                    start = True
                    if str[i] == '-':
                        i += 1
                        sign = -1
                elif str[i] != ' ':
                    return 0
            if start and i < len(str) and str[i].isnumeric():
                num += str[i]
            elif start:
                break
            i += 1

        order = len(num) - 1
        res = 0
        for i in range(len(num)):
            res += int(num[i]) * 10 ** (order - i)
        if res >= 2 ** 31:
            return 2 ** 31 - 1
        elif res < -2 ** 31:
            return -2 ** 31
        else:
            return res * sign
        return 0

s = Solution()
print(s.myAtoi("+-2"))