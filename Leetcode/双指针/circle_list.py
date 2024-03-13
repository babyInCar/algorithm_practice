"""
请问如何判断一个单向链表是否有环
          1<-8
          |  ^
          |  |
5->3->7->2->6

"""

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Node:
    def hasCycle(self, head: ListNode) -> bool:
        p1 = head
        p2 = head.next.next

        while p2 is not None and p2.next is not None:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return True
        return False