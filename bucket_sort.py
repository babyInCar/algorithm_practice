# 排序算法中的桶排序，算法复杂度O(n+m) 一种不怎么常见，但是很值得了解的算法

def bucket_sort(array=[]):
    min_value = array[0]
    max_value = array[0]
    # 1.得到数组的最大值和最小值，并计算出差值
    for element in array:
        if element < min_value:
            min_value = element
        if element > max_value:
            max_value = element
    minus = max_value - min_value
    # 2. 创造桶
    bucket_list = []
    for i in range(0, len(array)):
        bucket_list.append([])
    # 3.向桶中放入元素
    bucket_len = len(array)
    for i in range(0, len(array)):
        num = int((array[i] - min_value) * (bucket_len-1)  / minus)
        bucket[num].append(array[num])
    # 4.对每个桶中的元素进行排序
    for bucket in bucket_list:
        bucket.sort()
    # 5.把排序后的元素组装输出
    sorted_list = []
    for sub_list in bucket_list:
        for element in sub_list:
             sorted_list.append(element)
     
     return sorted_list
soap_array = [4.12,6.421,0.0023,3.0,2.123,8.122,4.12,10.09]
print(bucket_sort(soap_array))
    
