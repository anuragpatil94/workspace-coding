"""
No: 28
Date: 12-01-2020

Problem:
    Design a class to implement a stack using only a single queue. Your class, 
    QueueStack, should support the following stack methods: 
    push() (adding an item), 
    pop() (removing an item), 
    peek() (returning the top value without removing it), and 
    empty() (whether or not the stack is empty).

TestCases:
    

Time Complexity:
    
Space Complexity:
    
"""


class QueueStack:
    def __init__(self):
        self.arr = []

    def push(self, val):
        self.arr.append(val)
        return -1

    def pop(self):
        if self.empty():
            return None
        l = len(self.arr)
        while l != 1:
            l -= 1
            self.arr.append(self.arr.pop(0))
        return self.arr.pop(0)

    def empty(self):
        if self.arr:
            return False
        return True

    def peek(self):
        if self.empty():
            return None
        return self.arr[-1]


qs = QueueStack()

print(qs.push(1))
print(qs.push(2))
print(qs.push(3))
print(qs.push(4))
print(qs.pop())
print(qs.pop())
print(qs.push(6))
print(qs.peek())
print(qs.pop())
print(qs.peek())
print(qs.empty())
