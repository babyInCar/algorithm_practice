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
  1.先给出砝码的列表，比如 
    2
    1 2
    2 1
  对应的所有砝码的列表为:[1,1,2]
 2.算出能表示的所有的结果
  {0}代表最初始值
  当遍历到1时，
  {0,0+1}
  再遍历到1时
  {0,1,0+1,1+2} = {0,1,2} 三种情况
  再遍历到2时
  {0,1,2,2,3,4} = {0,1,2,3,4} 五种情况
  {}  
"""

n = int(input())
weight_list = input().split(" ")
num_list = input().split(" ")
fama_list = []
for i in range(n):
    for item in range(int(num_list[i])):
        fama_list.append(weight_list[i])

total_set = {0}
for i in fama_list:
    temp_list = []
    for item in total_set:
        temp_list.append(item+int(i))
    total_set |= set(temp_list)
    # total_set = list(set(total_list))
print(len(total_set))


