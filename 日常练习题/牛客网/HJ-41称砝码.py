"""
描述
现有n种砝码，重量互不相等，分别为
m1, m2, m3…mn ；
每种砝码对应的数量为
x1, x2, x3...xn 。现在要用这些砝码去称物体的重量(放在同一侧)，问能称出多少种不同的重量。


注：
称重重量包括
0

输入描述：
对于每组测试数据：
第一行：n - -- 砝码的种数(范围[1, 10])
第二行：m1 m2 m3...mn - -- 每种砝码的重量(范围[1, 2000])
第三行：x1  x2  x3....xn - -- 每种砝码对应的数量(范围[1, 10])
输出描述：
利用给定的砝码可以称出的不同的重量数

示例1
输入：
2
1 2
2 1

输出：
5

说明：
可以表示出0，1，2，3，4五种重量。
"""

"""
  解题思路:
  
"""

n = int(input())
weight_list = input().split(" ")
num_list = input().split(" ")
fama_list = []
for i in range(n):
    for item in num_list:
        fama_list.append(weight_list[i])

total_list = [0]
for i in fama_list:
    temp_list = []
    for item in total_list:
        total_list.append(item+int(i))
        total_set = list(set(total_list))
print(len(total_list))


