class Recursion:
    def deleteMidEle(self, stack,k):
        # mid = int(len(stack)/2)
        if k == 1:
            stack.pop()
            return
        temp = stack.pop()
        self.deleteMidEle(stack,k-1)
        stack.append(temp)

from collections import deque
stack = deque()
stack.append(1)
stack.append(5)
stack.append(0)
stack.append(2)
stack.append(3)
class_obj = Recursion()
k = int(len(stack)/2)
class_obj.deleteMidEle(stack,k)
print(stack)

