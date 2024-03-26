"""
 面试出题企业：｛小米科技，武汉布奇｝
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
        # 判断临界条件
        if head is None:
            return None
        cur = head
        pre = None  # 模拟一个空的节点

        while cur.next:
            # 保存当前节点的指针
            tmp = cur.next
            # 当前指针反向指向左边的节点
            cur.next = pre
            # pre 指向空节点
            pre = cur
            # cur 向后移动一位
            cur = tmp
        return pre

