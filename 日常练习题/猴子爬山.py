"""
猴子爬山
题目描述：
一天一只顽猴想要从山脚爬到山顶，
途中经过一个有n个台阶的阶梯，
但是这个猴子有个习惯，每一次只跳1步或3步
试问？猴子通过这个阶梯有多少种不同的跳跃方式
"""


# 用动态规划的思路来解决问题
def monkeyClimb(n: int):
    """猴子爬山"""
    if n  == 0:
        return 1
    elif n <= 2:
        return 1
    elif n == 3:
        return 2

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2

    # 填充dp数组
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 3]

    return dp[n]


if __name__ == '__main__':
    print(monkeyClimb(4))