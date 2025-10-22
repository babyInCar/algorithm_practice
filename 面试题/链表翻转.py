

class Solution:
    class ListNode:
        def __init__(self, data):
            self.data = data
            self.next = None

    def reverseList(self, head: ListNode):
        # 边界条件
        # if head is None:
        #     return None
        # cur = head
        # pre = None
        #
        # while cur.next:
        #     tmp = cur.next
        #     cur.next= pre
        #     pre = cur
        #     cur = tmp
        #
        # return pre

        if head is None:
            return None

        cur = head
        pre = None

        while cur.next:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre