"""
125.验证回文串

如果在将所有大写字符转换成小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个回文串

字母和数字都属于字母数字字符。
给你一个字符串，如果它是回文串，返回true；否则返回False、
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False
        s = "".join(filter(str.isalnum, s)).lower()
        str_len = len(s)
        for index, sub_str in enumerate(s[:int(str_len/2)]):
            if s[index] != s[str_len-index-1]:
                return False
            self.isPalindrome(s[index:str_len-index-1])
        return True

s = Solution()
s1 = "A man, a plan, a canal: Panama"
s2 = "abdcde"
print(s.isPalindrome(s1))