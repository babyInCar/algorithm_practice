
import sys

# 方向数组（右、下、左、上）
directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def dfs(plaintext, index, x, y, visited, path):
    global min_cipher_path, found
    # 找到一条完整路径
    if index == len(plaintext):
        current_path = " ".join(path)
        if not found or current_path < min_cipher_path:
            min_cipher_path = current_path
        found = True
        return
    #  边界检查、是否访问过、是否匹配当前明文字符
    if x < 0 or y < 0 or x >= cipher_size or y >= cipher_size or visited[x][y] or cipher_book[x][y] != plaintext[index]:
        return

    visited[x][y] = True
    path.append(f"{x} {y}")

    for dx, dy in directions:
        dfs(plaintext, index + 1, x + dx, y + dy, visited, path)

    visited[x][y] = False
    path.pop()  # 回溯

if __name__ == "__main__":
    input_data = sys.stdin.read().splitlines()
    # 明文长度
    plaintext_length = int(input_data[0])
    # 明文数据
    plaintext = list(map(int, input_data[1].split()))
    # 密文长度
    cipher_size = int(input_data[2])
    # 密文矩阵
    cipher_book = [list(map(int, input_data[i + 3].split())) for i in range(cipher_size)]

    visited = [[False] * cipher_size for _ in range(cipher_size)]
    min_cipher_path = ""
    found = False

    for i in range(cipher_size):
        for j in range(cipher_size):
            # 尝试进行递归搜寻
            if cipher_book[i][j] == plaintext[0]:
                dfs(plaintext, 0, i, j, visited, [])

    print(min_cipher_path if found else "error")

