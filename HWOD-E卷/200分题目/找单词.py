"""

给一个字符串和一个二维字符数组，如果该字符串存在于该数组中，则按字符串的字符顺序输出字符串每个字符所在单元格的位置下标字符串，如果找不到返回字符串“N”。

1.需要按照字符串的字符组成顺序搜索，且搜索到的位置必须是相邻单元格，其中“相邻单元格”是指那些水平相邻或垂直相邻的单元格。

2.同一个单元格内的字母不允许被重复使用。

3.假定在数组中最多只存在一个可能的匹配。

输入描述
第1行为一个数字N指示二维数组在后续输入所占的行数。

第2行到第N+1行输入为一个二维大写字符数组，每行字符用半角,分割。

第N+2行为待查找的字符串，由大写字符组成。

二维数组的大小为N*N，0<N<=100。

单词长度K，0<K<1000。
"""

from collections import deque


def dfs(matrix, x, y, visited, target, index, path, result):
    if (x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or
            visited[x][y] or matrix[x][y] != target[index]):
        return

        # 标记当前节点为已访问
    visited[x][y] = True
    path.append(f"{x},{y}")  # 将当前坐标加入路径

    # 如果已经匹配到目标字符串的最后一个字符
    if index == len(target) - 1:
        result.append(path.copy())  # 将当前路径加入结果
    else:
        # 向四个方向递归搜索
        dfs(matrix, x + 1, y, visited, target, index + 1, path, result)  # 下
        dfs(matrix, x - 1, y, visited, target, index + 1, path, result)  # 上
        dfs(matrix, x, y + 1, visited, target, index + 1, path, result)  # 右
        dfs(matrix, x, y - 1, visited, target, index + 1, path, result)  # 左

    # 回溯：撤销当前节点的访问标记，并移除当前坐标
    visited[x][y] = False
    path.pop()
    # if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix) or visited[x][y]:
    #     return
    #
    # # 标记当前节点为已访问
    # visited[x][y] = True
    # current_words += matrix[x][y]
    # if target.startswith(current_words):
    #     # print("=====")
    #     # current_words += matrix[x][y]
    #     ans.append(f"{x},{y},")
    #     dfs(matrix, x+1, y, visited, target, ans, current_words)
    #     dfs(matrix, x-1, y, visited, target, ans, current_words)
    #     dfs(matrix, x, y+1, visited, target, ans, current_words)
    #     dfs(matrix, x, y-1, visited, target, ans, current_words)
    #
    # # 回溯： 撤销当前节点的访问标记
    # visited[x][y] = False
    # current_words = current_words[:-1]


def dfs_traversal(matrix, n, target_word):
    ans = []
    result = []
    if not matrix:
        return
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dfs(matrix, i, j, visited, target_word, 0, [], result)
    # dfs(matrix, 0, 0, visited, target_word, 0, ans, result)
    return "，".join(result[0]) if result else "N"


def bfs(n, words, target_word):
    ans = ""
    directions = [(1, 0), (0, 1)]
    visited = [[False] * n for _ in range(n)]

    queue = deque([(0, 0)])
    visited[0][0] = True
    current_words = ""
    print(words)
    print("====")
    while queue:

        x, y = queue.popleft()
        # print(f"==={x}, {y}")

        if target_word.startswith(current_words + words[x][y]):
            current_words += words[x][y]
            ans += f"{x},{y},"

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
    return ans if ans else "N"


if __name__ == '__main__':
    m = int(input())
    mountain = [list(map(str, input().split(','))) for _ in range(m)]
    target_words = input()
    # 计算结果并输出
    ans = dfs_traversal(mountain, m, target_words)
    print(f"{ans}")


