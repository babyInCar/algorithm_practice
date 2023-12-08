"""
560. 和为 K 的子数组
给你一个整数数组nums 和 一个整数k,请你统计并返回该数组中和为k的子数组的个数

"""
from typing import List
def subarraySum(nums: List[int], k: int) -> int:
    pre, count = 0, 0
    mp = {0: 1}
    for i in range(len(nums)):
        pre += nums[i]
        if pre - k in mp:
            count += mp[pre - k]
        mp[pre] = mp.get(pre, 0) + 1
    print(mp)
    return count
print(subarraySum([1,-1,0],2))