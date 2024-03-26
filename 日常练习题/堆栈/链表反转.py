"""
【单向链表的翻转】给定单链表的头节点 head ，请反转链表，并返回反转后的链表的头节点。
a->b->c->d->e

    a   b   c   d   e
  cur  tmp             pre

翻转后为：a<-b<-c<-d<-e

输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
"""

class Solution:
    class ListNode:
        def __init__(self, data):
            self.data = data
            self.next = None

    def reverseList(self, head: ListNode):
        if head is None:
            return None
        cur = head
        pre = None

        while cur:
            tmp = cur.next








