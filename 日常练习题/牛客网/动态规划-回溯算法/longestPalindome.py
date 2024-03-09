class Solution:
    def getLongestPalindrome(self , A: str) -> int:
        # write code here
        # 解法一： 时间复杂度高，但是思路更简单
        count = []
        flag = 1
        n = len(A)
        # i这里可以理解为步长，每次取固定步长的字符串比较，相等的话，则说明相等
        for i in range(1, n+1):
            for j in range(0, n-i+1):
                if A[j:j+i] == A[j:j+i][::-1]:
                    flag = i
                else:
                    continue
            count.append(flag)
        return max(count)

        # 解法二： 时间复杂度更小，但是更复杂
        t = "#"

        for c in A:
            t += c + "#"
        n = len(t)

        # 初始化状态数组p，其中p[i]表示以i为中心的回文子串的最远右边界
        p = [0] * n

        # 中心扩展算法，记录当前回文半径最大值
        center, max_right = 0, 0

        for i in range(1, n - 1):
            mirror = 2 * center - i
            if max_right > i:
                p[i] = min(max_right - i, p[mirror])
            else:
                p[i] = 0

            # 扩展 palindrome as much as possible
            while i - p[i] >= 0 and i + p[i] < n and t[i - p[i]] == t[i + p[i]]:
                p[i] += 1

            # 更新中心和最右边界
            if i + p[i] > max_right:
                center, max_right = i, i + p[i]

        # 找到最长回文子串的实际长度（不包括预处理时插入的#）
        max_length = max(p) - 1 if max(p) > 0 else 0

        return max_length

s = Solution()
# str1 = "baabccc"
str1 = "ababc"
print(s.getLongestPalindrome(str1))