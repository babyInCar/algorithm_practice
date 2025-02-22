

def dfs(matrix, x, y, visited, target, index, path, result):
    # 检查当前坐标是否在矩阵范围内，是否已经访问过，以及当前字符是否匹配目标字符
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


def dfs_traversal(matrix, target_word):
    if not matrix or not target_word:
        return "N"

    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    result = []  # 存储所有匹配的路径

    # 从每个可能的起点开始搜索
    for i in range(rows):
        for j in range(cols):
            dfs(matrix, i, j, visited, target_word, 0, [], result)

    # 如果找到匹配路径，返回第一条路径的坐标
    if result:
        return ",".join(result[0])
    else:
        return "N"


if __name__ == '__main__':
    m = int(input())
    mountain = [list(map(str, input().split(','))) for _ in range(m)]
    target_words = input()
    # 计算结果并输出
    ans = dfs_traversal(mountain, target_words)
    print(f"{ans}")