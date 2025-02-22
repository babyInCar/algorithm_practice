"""
疫情期间需要大家保证一定的社交距离，公司组织开交流会议。
座位一排共 N 个座位，编号分别为 [0, N - 1] 。
要求员工一个接着一个进入会议室，并且可以在任何时候离开会议室。

满足：
每当一个员工进入时，需要坐到最大社交距离（最大化自己和其他人的距离的座位）；
如果有多个这样的座位，则坐到索引最小的那个座位。
输入描述
会议室座位总数 seatNum

1 ≤ seatNum ≤ 500
员工的进出顺序 seatOrLeave 数组

元素值为 1，表示进场

元素值为负数，表示出场（特殊：位置 0 的员工不会离开）

例如 -4 表示坐在位置 4 的员工离开（保证有员工坐在该座位上）

输出描述
最后进来员工，他会坐在第几个位置，如果位置已满，则输出-1。

"""


def get_largest_social_distance(n, a):
    """计算最大社交安全距离"""
    vis = [0] * (n+1)
    # 记录最后一个进入的人的座位
    ans = 0

    for val in a:
        if val == 1:  # 有新人进入
            lmaxv = 0
            maxv = 0
            idx = 1  # 当前选择的座位的索引

            if vis.count(1) == 0:
                vis[idx] = 1
                ans = idx
                continue

            # 遍历所有座位，寻找最大社交安全距离的位置
            rmaxv = 0
            for i in range(1, n+1):
                if vis[i] == 0:
                    ldist = i - lmaxv  # 左边距
                    rdist = rmaxv - i  # 右边距
                    if rmaxv == n + 1:  # 右边没有被占用的位置
                        rdist = n * 10
                    dist = min(ldist, rdist)
                    if dist > maxv:
                        maxv, idx = dist, i
                else:
                    lmaxv = i
                    rmaxv = lmaxv + 1
                    while rmaxv <= n and vis[rmaxv] == 0:
                        rmaxv += 1
            # 选定座位，更新状态
            vis[idx] = 1
            ans = idx

        else:
            vis[-val + 1] = 0
    return ans-1


if __name__ == '__main__':
    n = int(input())
    a = eval(input())

    print(get_largest_social_distance(n, a))

