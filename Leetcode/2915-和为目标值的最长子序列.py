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
from typing import List

# def lengthOfLongestSubsequence(nums: List[int], target: int) -> int:
#     d = {0: -1}  # 初始化字典，键为前缀和，值为对应的下标
#     s = 0  # 初始前缀和为0
#     max_length = -1  # 初始最大子序列长度为-1
#     for i, num in enumerate(nums):
#         s += num  # 更新前缀和
#         if s - target in d:  # 如果前缀和减去目标值在字典中，说明找到了一个子序列
#             max_length = max(max_length, i - d[s - target])  # 更新最大子序列长度
#         d[s] = i  # 将前缀和以及对应的下标存入字典
#     print(d)
#     return max_length

def find_subsequences(nums, target):
   result = []
   n = len(nums)

   def backtrack(start, path):
       if sum(path) == target:
           result.append(len(path[:]))
           return
       if start == n:
           return

       for i in range(start, n):
           path.append(nums[i])
           backtrack(i + 1, path)
           path.pop()

   backtrack(0, [])
   return max(result)

nums = [3,7,6,7,2,2,2,10,7,10,8,7,7,10,7,3,1,2,8,3,5,1,5,8,4,8,8,7,6,2,4,8,10,9,5,9,2,3,1,7,4,10,7,5,2,8,6,5,1,3,5,9,9,10,6,10]
target = 162
print(find_subsequences(nums, target))


# print(find_subsequences(nums=[3,5,2,3,4], target=12))