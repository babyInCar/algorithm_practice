"""
313 小米面试题
给出一个链表，请用代码实现如何将链表原地翻转
备注：
1.不能使用递归
2.链表只能遍历一次

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:

    # 该题目想要考察的点是双指针的解法
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        cur, pre = head, None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

