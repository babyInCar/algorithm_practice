


def climb(n):
    """计算总共有多少种方案"""
    if n == 0:
        return 1
    if n <= 2:
        return 1
    if n == 3:
        return 2
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-3]
    return dp[n]


if __name__ == '__main__':
    n = int(input())
    print(climb(n))

