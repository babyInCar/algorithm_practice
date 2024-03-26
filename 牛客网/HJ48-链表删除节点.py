"""
描述
输入一个单向链表和一个节点的值，从单向链表中删除等于该值的节点，删除后如果链表中无节点则返回空指针。

链表的值不能重复。

构造过程，例如输入一行数据为:
6 2 1 2 3 2 5 1 4 5 7 2 2
则第一个参数6表示输入总共6个节点，第二个参数2表示头节点值为2，剩下的2个一组表示第2个节点值后面插入第1个节点值，为以下表示:
1 2 表示为
2->1
链表为2->1

3 2表示为
2->3
链表为2->3->1

5 1表示为
1->5
链表为2->3->1->5

4 5表示为
5->4
链表为2->3->1->5->4

7 2表示为
2->7
链表为2->7->3->1->5->4
最后的链表的顺序为 2 7 3 1 5 4
最后一个参数为2，表示要删掉节点为2的值
删除 结点 2

则结果为 7 3 1 5 4
数据范围：链表长度满足1≤n≤1000，，节点中的值满足 0<=val<=10000

"""

link_list = []
num_list = input().split(' ')
num_total = int(num_list[0])
link_list.append(num_list[1])
new_num_list = num_list[2:]
for i in range(0, (num_total-1)*2, 2):
    s1 = new_num_list[i]
    s2 = new_num_list[i+1]
    pos = link_list.index(s2)
    if pos == len(link_list)-1:
        link_list.append(s1)
    else:
        link_list.insert(pos+1, s1)
link_list.remove(num_list[-1])
# print(link_list)
for item in link_list:
    print(int(item), end=" ")



