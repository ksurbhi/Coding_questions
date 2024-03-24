class Recursion:
    def sort(self, arr):
        if len(arr)<=1:
            return
        tmp = arr.pop()
        self.sort(arr)
        self.insert(arr,tmp)

    def insert(self, arr, tmp):
        if len(arr)==0 or arr[-1] <=tmp:
            arr.append(tmp)
            return 
        tmp1 = arr.pop()
        self.insert(arr, tmp)
        arr.append(tmp1)


# arr = [1,5,0,2,6]

from collections import deque
stack = deque()
stack.append(1)
stack.append(5)
stack.append(0)
stack.append(2)
stack.append(3)
class_obj = Recursion()
class_obj.sort(stack)
print(stack)

