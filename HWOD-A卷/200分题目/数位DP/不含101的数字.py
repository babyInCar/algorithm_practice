

MAX_LEN = 32
dp = [[[-1] * 2 for _ in range(2)] for _ in range(MAX_LEN)]
binary = [0] * MAX_LEN


# 递归搜索 pos 当前位置 limit 之前是否为最大值标志(此标志会限制当前取值范围)  pre  前一位的值 前两位值
def dfs(pos, limit, pre, prepre):
    if pos == -1:
        return 1  # 递归结束，找到一个有效方案
    # 利用记忆化数组缓存直接范围
    if not limit and dp[pos][pre][prepre] != -1:
        return dp[pos][pre][prepre]

    maxDigit = binary[pos] if limit else 1
    count = 0

    for i in range(maxDigit + 1):
        if i == 1 and pre == 0 and prepre == 1:
            continue  # 跳过非法情况
        count += dfs(pos - 1, limit and (i == maxDigit), i, pre)

    if not limit:
        dp[pos][pre][prepre] = count
    return count


# 计算 0~num 内的合法数字个数
def digitSearch(num):
    global dp, binary
    for i in range(MAX_LEN):
        for j in range(2):
            for k in range(2):
                dp[i][j][k] = -1

    binary = [0] * MAX_LEN
    len_ = 0

    while num:
        binary[len_] = num & 1
        num >>= 1
        len_ += 1

    return dfs(len_ - 1, 1, 0, 0)


if __name__ == "__main__":
    L, R = map(int, input().split())
    print(digitSearch(R) - digitSearch(L - 1))

