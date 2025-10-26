"""
有一种特殊的加密算法，明文为一段数字串，经过密码本查找转换，生成另一段密文数字串。

规则如下：
明文为一段数字串由 0~9 组成
密码本为数字 0~9 组成的二维数组
需要按明文串的数字顺序在密码本里找到同样的数字串，密码本里的数字串是由相邻的单元格数字组成，上下和左右是相邻的，
注意：对角线不相邻，同一个单元格的数字不能重复使用。

每一位明文对应密文即为密码本中找到的单元格所在的行和列序号（序号从0开始）组成的两个数宇。
如明文第 i 位 Data[i] 对应密码本单元格为 Book[x][y]，则明文第 i 位对应的密文为X Y，X和Y之间用空格隔开。

如果有多条密文，返回字符序最小的密文。
如果密码本无法匹配，返回"error"。
请你设计这个加密程序。

示例1：

密码本：
0 0 2
1 3 4
6 6 4

输入示例：
2
0 3
3
0 0 2
1 3 4
6 6 4

输出示例：
0 1 1 1

思路：
1. 明文和密文数据
2.
"""


def backtrack(plain_text, index, x, y, visited, path,state):
    # 方向 右边，下边， 👈🏻, 上
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # global min_cipher_path, found
    # # 找到一条完整路径

    if index == len(plain_text):
        current_path = " ".join(path)
        if not state.get('found') or current_path < state.get('min_cipher_path'):
            state['min_cipher_path'] = current_path
        state['found'] = True
        return

    if x < 0 or y < 0 or x >= cipher_size or y >= cipher_size or visited[x][y] or matrix[x][y] != plain_text[index]:
        return
    # if x<0 or y <0 or x>=cipher_size or y >= cipher_size or visited[x][y] or matrix[x][y] != plain_text[index]:
    #     return

    visited[x][y] = True
    path.append(f"{x} {y}")

    for dx, dy in directions:
        backtrack(plain_text, index + 1, x + dx, y + dy, visited, path, state)

    visited[x][y] = False
    path.pop()  # 回溯


if __name__ == '__main__':
    origin_len = int(input())
    plain_text = list(map(int, input().split()))
    cipher_size = int(input())
    matrix = [list(map(int, input().split())) for _ in range(cipher_size)]
    visited = [[False]*cipher_size for _ in range(cipher_size)]
    # min_cipher_path = ""
    found = False
    state = {
        'found': False,
        'min_cipher_path': ""
    }
    for i in range(cipher_size):
        for j in range(cipher_size):
            if matrix[i][j] == plain_text[0]:
                backtrack(plain_text, 0, i, j, visited, [], state)
    print(state.get('min_cipher_path') if state.get('found') else "error")