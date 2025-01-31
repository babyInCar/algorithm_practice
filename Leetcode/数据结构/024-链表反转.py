

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        cur = head
        pre = None

        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre