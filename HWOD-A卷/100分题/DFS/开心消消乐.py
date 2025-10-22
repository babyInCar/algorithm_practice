
"""
4 4
1 1 0 0 
0 0 0 1 
0 0 1 1 
1 1 1 1

"""
import sys
sys.setrecursionlimit(10**6)   # 设置递归深度


dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]


def dfs(grid, x, y, row, col):
    grid[x][y] = 0
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] == 1:
            dfs(grid, nx, ny, row, col)


def main():
    """通过DFS算法来实现"""
    row, col = map(int, input().split(" "))
    grid = [list(map(int, input().split())) for _ in range(row)]
    print(grid)
    res = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                res += 1
                dfs(grid, i, j, row, col)
    print(res)


if __name__ == '__main__':
    main()



