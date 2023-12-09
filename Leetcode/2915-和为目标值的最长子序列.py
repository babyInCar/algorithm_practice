"""
2915-和为目标值的最长子序列的长度
给你一个下表从0开始的整数数组nums和一个整数target
返回和为target的nums子序列中，子序列长度的最大值。如果不存在和为target的子序列，返回-1.
子序列指的是从原数组中删除一些或者不删除任何元素后，剩余元素保持原来的顺序构成的数组

示例1：
输入：nums = [1,2,3,4,5],target=9
输出：3

示例2：
输入：nums=[4,1,3,2,1,5], target=7
输出：4
解释：总共有 5 个子序列的和为 7 ：[4,3] ，[4,1,2] ，[4,2,1] ，[1,1,5] 和 [1,3,2,1] 。最长子序列为 [1,3,2,1] 。所以答案为 4 。

示例3：
输入：nums = [1,1,5,4,5],target=3
输出：-1
"""

def find_subsequences(nums, target):
    dp = [-1] * (target+1)
    dp[0] = 0
    s = 0
    for x in nums:
        s = min(s + x, target)
        for j in range(s, x-1, -1):
            if dp[j - x] != -1:
                dp[j] = max(dp[j], dp[j-x] + 1)
            print(dp)
    return dp[target]

# nums = [3,5,2,3,4]
nums = [1,2,3,4,5]
# nums = [1,1,5,4,5]
# nums = [7,1,1]
target = 9
print(find_subsequences(nums, target))
# print(find_subsequences(nums=[3,5,2,3,4], target=12))