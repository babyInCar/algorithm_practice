"""
难度：mid
给定两个字符串str1和str2,输出两个字符串的最长公共子串
题目保证str1和str2的最长公共子串存在且唯一。

示例1:
输入： "1AB2345CD","12345EF"
返回值："2345"
"""

class Solution:
    def LCS(self, str1: str, str2: str) -> str:
        # write code here
        m = len(str1)
        ret_str = ""
        left = 0
        for i in range(1, m+1):
            if str1[left:i+1] in str2:
                ret_str = str1[left:i+1]
            else:
                left += 1
        return ret_str


s = Solution()
print(s.LCS("sdfsadf4S67CVmqx3OGJ6RKq15N517ZWxL848cuvYBPoz4l6ZS64w97rDesnclMw4qxy8xS2tJVZtVZH5Jo3vKKl5ul29QmfkFr52mtXF7Mxw61238124123", "4S67CVmqx3OGJ6RKq15N517ZWxL848cuvYBPoz4l6ZS64w97rDesnclMw4qxy8xS2tJVZtVZH5Jo3vKKl5ul29QmfkFr52mtXF7Mxw6#$1234123"))