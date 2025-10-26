import sys

sys.setrecursionlimit(10**7)

# 树状数组 更新值
def update(tree, index, delta):
    n = len(tree) - 1
    while index <= n:
        tree[index] += delta
        index += index & -index

# 树状查询组 区间和
def query(tree, index):
    res = 0
    while index:
        res += tree[index]
        index -= index & -index
    return res


def main():
    n = int(input())

    size = n
    fenw0_odd = [0] * (size + 1)  # 全奇数序列
    fenw1_even = [0] * (size + 1)  # 全偶数序列

    fenw2_even = [0] * (size + 1)  # 奇偶交替，下一位需为奇数
    fenw2_odd = [0] * (size + 1)   # 奇偶交替，下一位需为偶数

    ans0 = ans1 = ans2 = 0

    for x in range(1, n + 1):
        half = x // 2
        if x % 2 == 1:  # x 是奇数
            dp0_val = query(fenw0_odd, half)
            dp2_val = query(fenw2_even, half)

            update(fenw0_odd, x, 1 + dp0_val)
            update(fenw2_odd, x, 1 + dp2_val)

            if x == n:
                ans0 = dp0_val
                ans2 = dp2_val
        else:  # x 是偶数
            dp1_val = query(fenw1_even, half)
            dp2_val = query(fenw2_odd, half)

            update(fenw1_even, x, 1 + dp1_val)
            update(fenw2_even, x, 1 + dp2_val)

            if x == n:
                ans1 = dp1_val
                ans2 = dp2_val

    total_sequences = 1 + ans0 + ans1 + ans2
    print(total_sequences)


if __name__ == "__main__":
    main()

