# 用栈来实现队列

class Queue:
    def __init__(self) -> None:
        self.in_stack = []
        self.out_stack = []
    
    def in_queue(self, element):
        self.in_stack.append(element)
        # self.out_stack.append(self.in_stack.pop())

    def out_queue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

q1 = Queue()
q1.in_queue(5)
q1.in_queue(2)
q1.in_queue(3)
print(q1.in_stack)
print(q1.out_queue())
print(q1.out_stack)
