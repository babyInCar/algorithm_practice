"""
给定一个长度为 n 的正整数数组 coins，每个元素表示对应位置的金币数量。
取位置
i 的金币时，假设左边一堆金币数量是L，右边一堆金币数量为
R，则获得
L∗cost[i]∗R的积分。如果左边或右边没有金币，则金币数量视为1。
请你计算最多能得到多少积分。

"""
from typing import List

class Solution:
    def getCoins(self, coins: List[int]) -> int:
        # write code here
        n = len(coins)
        coins = [1] + coins + [1]
        dp = [[0] * (n + 2) for _ in range(n+2)]
        for i in range(1, n+1):
            dp[i][i] = coins[i-1] * coins[i] * coins[i+1]

        for i in range(n, 0, -1):
            for j in range(i+1, n+1):
                left = dp[i+1][j] + coins[i-1] * coins[i] * coins[j+1]
                right = dp[i][j-1] + coins[i-1] * coins[j] * coins[j+1]
                dp[i][j] = max(left, right)
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k-1] + coins[i-1] * coins[k] * coins[j+1] + dp[k+1][j])
        return dp[1][n]


if __name__ == '__main__':
    sol = Solution()

    coins = [5, 6, 4, 8]
    res = sol.getCoins(coins)
    print(res)