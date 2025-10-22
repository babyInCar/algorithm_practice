class ListNode:
    """链表节点类"""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    """链表类"""

    def __init__(self):
        self.head = None  # 头节点

    def append(self, val):
        """在链表末尾添加节点"""
        if not self.head:
            self.head = ListNode(val)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = ListNode(val)

    def insert_node(self, val):
        if not self.head:
            self.head = ListNode(val)
            return

        current = self.head

        while current.next:
            pass


    def delete_node(self, val):

        if not self.head:
            return False

        if self.head.val == val:
            self.head = self.head.next
            return True

        current = self.head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
                return True
            current = current.next

        # if not self.head:
        #     return False
        #
        # if self.head.val == val:
        #     self.head = self.head.next
        #     return True
        #
        # # 删除中间节点或尾部节点
        # current = self.head
        #
        # while current.next:
        #     if current.next.val == val:
        #         current.next = current.next.next
        #         return True
        #     current = current.next
