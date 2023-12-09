"""
560. 和为 K 的子数组
给你一个整数数组nums 和 一个整数k,请你统计并返回该数组中和为k的子数组的个数

时间复杂度：O(n)
空间复杂度:O(n)
"""
# Python
from typing import List
def subarraySum(nums: List[int], k: int) -> int:
    pre, count = 0,0
    mp = {0:1}
    for i in range(len(nums)):
        pre += nums[i]
        if pre - k in mp:
            count += mp[pre-k]
        mp[pre] = mp.get(pre, 0) + 1
    return count
print(subarraySum([1,-1,0],0))


"""
解析：
该解法基于这样的逻辑：
因为是连续的数组求和，所以我假设
pre[i] 代表nums[0...i]的和，pre[j,i] 为满足条件的求和为k的情况
那么，pre[i] - pre[j-1] == k（按区间段的方式来理解）
移项之后，pre[j-1] == pre[i]-k,所以只要有pre[i] - k出现，那么我们就可以得出找到满足条件的pre[j,i]出现
所以通过python里面的dict，我们来做判断累加即可 
"""