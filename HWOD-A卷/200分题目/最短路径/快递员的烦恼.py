


import sys

def main():
    # 读取输入
    N, M = map(int, sys.stdin.readline().split())

    # 初始化图，默认所有路径为 -1
    graph = [[-1] * (N + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        graph[i][i] = 0  # 自己到自己距离为 0

    # 使用字典离散化 ID
    mp = {}

    # 读取投递站到客户的距离
    for i in range(N):
        id_, distance = map(int, sys.stdin.readline().split())
        mp[id_] = i + 1
        graph[0][mp[id_]] = distance
        graph[mp[id_]][0] = distance

    # 读取客户之间的距离
    for _ in range(M):
        start, end, distance = map(int, sys.stdin.readline().split())
        graph[mp[start]][mp[end]] = distance
        graph[mp[end]][mp[start]] = distance

    # Floyd-Warshall 算法计算最短路径
    for k in range(N + 1):
        for i in range(N + 1):
            for j in range(N + 1):
                if graph[i][k] == -1 or graph[k][j] == -1:
                    continue
                if graph[i][j] == -1:
                    graph[i][j] = graph[i][k] + graph[k][j]
                else:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    # 状态压缩 DP，dp[mask][cur] 表示访问过 mask 里的所有客户后，停在 cur 的最短路径
    dp = [[float('inf')] * (N + 1) for _ in range(1 << N)]
    dp[0][0] = 0  # 从起点出发

    for mask in range(1 << N):
        for cur in range(N + 1):
            if dp[mask][cur] == float('inf'):
                continue
            for next_ in range(N + 1):
                if graph[cur][next_] == -1:
                    continue
                if next_ == 0:
                    dp[mask][next_] = min(dp[mask][next_], dp[mask][cur] + graph[cur][next_])
                else:
                    next_mask = mask | (1 << (next_ - 1))
                    dp[next_mask][next_] = min(dp[next_mask][next_], dp[mask][cur] + graph[cur][next_])

    # 计算最终结果，遍历所有可能的终点
    end = (1 << N) - 1
    res = float('inf')
    for i in range(N + 1):
        if dp[end][i] != float('inf') and graph[i][0] != -1:
            res = min(res, dp[end][i] + graph[i][0])

    # 输出结果
    print(res)

if __name__ == "__main__":
    main()

