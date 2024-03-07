"""
请问如何判断一个单向链表是否有环
          1<-8
          |  ^
          |  |
5->3->7->2->6

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def getCircle():
    p1 = head.next
    p2 = head.next.next

    # while p1.next != p1.next