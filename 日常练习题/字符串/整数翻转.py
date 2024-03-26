"""


"""

class Solution:
    def reverse(self, x: int) -> int:
        if x < -2 ** 31 or x > 2 ** 31 - 1:
            return 0

        if x >= 0 and x < 10:
            return x
        str1 = str(x)
        # print(str1[-1:0:-1])
        str2 = str1[::-1] if x > 0 else '-' + str1[-1:0:-1]
        print(str2)
        return str2

s = Solution()
s.reverse(1534236469)