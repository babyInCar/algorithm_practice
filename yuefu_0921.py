# encoding=utf-8
# given a array like:foo = [{'name': 'bob', 'age': 20}, {'name': "alice", "age": 47}, {"name": "lucy", "age": 30}], please sort the elements by name or age
# 给定一个数组，foo = [{'name': 'bob', 'age': 20}, {'name': "alice", "age": 47}, {"name": "lucy", "age": 30}], 请分别按name和age排序输出

foo = [{'name': 'bob', 'age': 20}, {'name': "alice", "age": 47}, {"name": "lucy", "age": 30}]

def sort_by_given_key(foo, key):
       """
       @param: foo: 指定的列表
       @param: 需要排序的key
       @return: 排序后的数组
       """
       key_list = [item.get(key) for item in foo]
       key_list.sort()
       result_list = []
       for k in key_list:
           for f in foo:
               if f.get(key) == k:
                   result_list.append(f)
       return result_list

print(sort_by_given_key(foo, "age"))
print(sort_by_given_key(foo, "name"))