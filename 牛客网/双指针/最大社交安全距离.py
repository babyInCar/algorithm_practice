"""



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
                    ldist = i - lmaxv
                    rdist = rmaxv - i
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

