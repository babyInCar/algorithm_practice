"""
2913.数组不同元素数目的平方和 I
 给你一个下表从0开始的证书数组nums
 定义nums一个子数组的不同计数值如下：
 . 令num[i..j]表示nums中所有下表在i到j范围内的元素构成的子数组（满足0<=i<=j<nums.length），那么我们称子数组
 nums[i..j]中不同值的树木为nums[i..j]的不同计数。
 请你返回nums中所有子数组的不同计数的平方和。
 由于答案可能会很大，请你将它对10² + 7取余后返回.
 子数组指的是一个数组里面一段连续非空的元素序列。

 示例1：
输入: nums = [1,2,1]
输出: 15

解释：
六个子数组分别为：
[1]: 1个互不相同的元素。
[2]: 1个互不相同的元素
[1]: 1个互不相同的元素
[1,2]: 2个互不相同的元素
[2,1]: 2个互不相同的元素
[1,2,1]：2个互不相同的元素
所有不同计算的平方和为: 1²+1²+1²++2²+2²+2²=15
"""

import math
from typing import List
class Solution:
    import math
    def get_sub_arrays(self, arr: List[int]) -> List:
        sub_arrays = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr) + 1):
                sub_arrays.append(arr[i:j])
        return sub_arrays

    def sumCounts(self, nums: List[int]) -> int:
        sub_list = self.get_sub_arrays(nums)
        odd_list = []
        for item in sub_list:
            odd_list.append(len(set(item)))

        total = sum([int(math.pow(x, 2)) for x in odd_list])
        return total




