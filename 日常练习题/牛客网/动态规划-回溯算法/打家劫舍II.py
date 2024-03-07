"""
描述
你是一个经验丰富的小偷，准备偷沿湖的一排房间，每个房间都存有一定的现金，为了防止被发现，你不能偷相邻的两家，即，如果偷了第一家，就不能再偷第二家，如果偷了第二家，那么就不能偷第一家和第三家。沿湖的房间组成一个闭合的圆形，即第一个房间和最后一个房间视为相邻。
给定一个长度为n的整数数组nums，数组中的元素表示每个房间存有的现金数额，请你计算在不被发现的前提下最多的偷窃金额。

数据范围：数组长度满足1≤n≤2×10*5，数组中每个值满足1<=nums[i]<=5000

示例1
输入： [1,2,3,4]
返回值：6
说明：最优方案是偷第 2 4 个房间

示例2
输入：[1,3,6]
返回值：6
说明：由于 1 和 3 是相邻的，因此最优方案是偷第 3 个房间
"""
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        condition1 = self.get_max_result(nums, 0)
        condition2 = self.get_max_result(nums, 1)
        return max(condition1, condition2)

    def get_max_result(self, nums, start):
        dp = [0 for i in range(len(nums)+1)]
        # print(len(nums))
        # print(len(dp))
        if start == 0:
            # 偷第一家, 不偷最后一家，初始状态为 nums[0]
            dp[1] = nums[0]
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])  # 状态转移方程
            return dp[len(nums)-1]
        else:
            # 不偷第一家，偷最后一家
            # 初始状态为0
            dp[1] = 0
            for i in range(2, len(nums)+1):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
            return dp[len(nums)]


if __name__ == '__main__':
    # 测试代码
    nums = [43, 4, 4, 1, 26, 29, 24, 44, 52, 12]
    # nums = [19,43,94,4,34,33,91,75,38,79]
    s = Solution()
    print(s.rob(nums))