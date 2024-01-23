"""
 空汽水瓶问题：
 三个空汽水瓶可以换一瓶汽水，允许向老板借空瓶子，但是必须换。
 小张手上有n个空汽水瓶，他想最多可以换多少瓶汽水。
 数据范围：输入的正整数满足1 <= n <= 1000

 输入描述：
    输入文件最多包含 10 组测试数据，每个数据占一行，仅包含一个正整数 n（ 1<=n<=100 ），表示小张手上的空汽水瓶数。n=0 表示输入结束，你的程序不应当处理这一行。
    输入例子：
 输出描述：
    对于每组测试数据，输出一行，表示最多可以喝的汽水瓶数。如果一瓶也喝不到，输出0。

 示例：
    3
    10
    81
    0

    输出例子：
    1
    5
    40
"""
import math

"""
    分析：
    这种是典型的递归算法问题
"""
import sys
from typing import List

res_list = []
def calc_bottles(raw_list:List, res):
    if input <= 1:
        return
    elif input == 2:
        res += 1
    else:
        res_list.append(math.floor(input / 3))
        input = math.floor(input / 3)
        print("input is:", input)
        calc_bottles(input, res)
    return res_list

for line in sys.stdin:
    raw_list = []
    if int(line) == 0:
        break
    raw_list.append(int(line))
    res_list = calc_bottles(raw_list)
    for res in res_list:
        print(res)