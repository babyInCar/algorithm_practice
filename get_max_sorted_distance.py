# 给出一个无序数组，请给出排序后最大相邻差值

# 分析：该问题虽然是求排序后最大相邻差值，但其实我们并不用真的排序，借助桶排序的思想，我们可以把接近的元素放在相同的桶里面，求每个桶的最大值和最小值，那前一个桶的最大值和后一个桶的最小值进行比较，最大的即为我们的答案

class Bucket:
    def __init__(self):
        self.min = None
        self.max = None
def get_max_sorted_distance(array=[]):
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
        bucket_list.append(Bucket())
    for i in range(0, len(array)):
         index = int((array[i] - min_value) * (len(array)-1)  / minus)
         if bucket_list[index].min is None or bucket_list[index].min > array[i]:
             bucket_list[index].min = array[i]
         if bucket_list[index].max is None or bucket_list[index].max < array[i]:
             bucket_list[index].max = array[i]
   # 4.遍历桶，找到最大差值
    left_max = bucket_list[0].max
    max_distance = 0
    for i in range(1, len(bucket_list)):
        if bucket_list[i].min is None:
          continue
        if bucket_list[i].min - left_max > max_distance:
           max_distance = bucket_list[i].min - left_max
        left_max = bucket_list[i].max
    return max_distance      
  
soap_array = [2,6,3,5,10,9]
print(get_max_sorted_distance(soap_array))
