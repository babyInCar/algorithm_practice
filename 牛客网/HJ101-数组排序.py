"""
HJ101 输入整型数组和排序标识，对其元素按照升序或降序进行排序
描述
输入整型数组和排序标识，对其元素按照升序或降序进行排序

数据范围：
1≤n≤1000 ，元素大小满足0≤val≤100000
输入描述：
第一行输入数组元素个数
第二行输入待排序的数组，每个数用空格隔开
第三行输入一个整数0或1。0代表升序排序，1代表降序排序

输出描述：
输出排好序的数字

示例1
输入：8
1 2 4 9 3 55 64 25
0
输出：1 2 3 4 9 25 55 64
"""
a = int(input())
input_list = [int(item) for item in input().split(" ")]
rank_order = int(input())
if rank_order == 0:
    input_list.sort()
    input_list = map(str, input_list)
elif rank_order == 1:
    input_list.sort(reverse=True)
    input_list = map(str, input_list)
print(" ".join(input_list))