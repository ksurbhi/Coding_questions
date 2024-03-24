class Recursion:
    def reverseStack(self, stack):
        if len(stack) <= 1:
            return
        temp = stack.pop()
        self.reverseStack(stack)
        self.insert(stack, temp)

    def insert(self,stack, temp):
        if len(stack) == 0:
            stack.append(temp)
            return
        temp1 = stack.pop()
        self.insert(stack,temp)
        stack.append(temp1)

from collections import deque
stack = deque()
stack.append(1)
stack.append(5)
stack.append(0)
stack.append(2)
stack.append(3)
print(stack)
class_obj = Recursion()
k = int(len(stack)/2)
class_obj.reverseStack(stack)
print(stack)

