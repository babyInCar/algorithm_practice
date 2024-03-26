
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def last_child(self, m:int, n:int):
        head = Node(0)
        current = head
        for i in range(1, n):
            current.next = Node(i)
            current = current.next
        current.next = head

        while current.next != current:
            for _ in range(m-1):
                current = current.next
            current.next = current.next.next

        return current.value

## 解法2：递归实现
def last_child2(n:int, m:int):
    if n == 0:
        return 0
    else:
        # tmp = (last_child2(n-1, m) + m) % n
        # print(tmp)
        return (last_child2(n-1, m) + m) % n

m = 3
n = 5
s = Solution()
print(s.last_child(m, n))
print(last_child2(n, m))