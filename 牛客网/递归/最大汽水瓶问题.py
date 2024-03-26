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

"""
    分析：
    这种是典型的递归算法问题
"""

def calc_sum(input:int):
    if input <= 1:
        return 0
    elif input == 2:
        return 1
    else:
        total = input // 3
        remainder = input % 3
    return total + calc_sum(total + remainder)

# while True:
#     input_num = int(input())
#     if input_num == 0:
#         break
#     print(calc_sum(input_num))

# for res in res_list:
#     print(res)

# 解法二：
"""
不用递归来解决问题
"""
def max(n:int):
    total = 0
    while n >= 3:
        total += n // 3
        n = n % 3 + n // 3
    # 不足三瓶，向老板借一瓶
    if n == 2:
        total += 1
    return total

while True:
    input_num = int(input())
    if input_num == 0:
        break
    print(max(input_num))