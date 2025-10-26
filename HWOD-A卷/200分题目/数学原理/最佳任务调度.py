
"""

输入：
2,2,2,3
2

输出：
7
"""


import sys


def dispatch():
    ans = input().split(',')
    n = int(input())

    count = len(ans)
    mp = {}

    # 统计每个字符出现的次数
    for word in ans:
        mp[word] = mp.get(word, 0) + 1

    nums = sorted(mp.values())

    # 统计最大值数量
    len_count = 1
    for i in range(len(nums) -2, -1, -1):
        if nums[i] != nums[i-1]:
            break
        len_count += 1

    res = max(count, (n+1)*(nums[-1]-1)+len_count)
    print(res)


if __name__ == "__main__":
    dispatch()

