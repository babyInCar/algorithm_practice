"""
28. 找出字符串中第一个匹配项的下标

题目描述：
给定两个字符串haystack和needle，请你在haystack字符串中找出needle字符串的第一个匹配的下标（下标从0开始）。
如果needle不是haystack的一部分，返回-1。

示例1：
    输入：haystack = "sadbutsad", needle="sad"
    输出:0
    解释："sad"在下标0和6处匹配。第一个匹配项的下标是0，所以返回0

示例2：
    输入：haystack = "leetcode", needle="leeto"
    输出: -1
    解释：leeto没有在leetcode中出现，所以返回-1
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        if needle == haystack[:len(needle)]:
            return 0
        tmp = self.strStr(haystack[1:], needle)
        return -1 if tmp == -1 else tmp + 1

s = Solution()
print(s.strStr("badbutsad", "sad"))