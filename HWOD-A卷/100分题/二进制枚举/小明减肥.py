"""


"""

# 快速求出对应数字1的位置
def count_ones_and_positions(n):
    positions = []
    index = 0
    while n:
        if n & 1:
            positions.append(index)
        n >>= 1
        index += 1
    return positions

n, t, k = map(int, input().split())
ans = list(map(int, input().split()))

res = 0
for i in range(1, 1 << n):
    pos = count_ones_and_positions(i)
    # 选取运动数不等于k
    if len(pos) != k:
        continue
    total = sum(ans[j] for j in pos)
    if total == t:
        res += 1

print(res)

