from collections import deque

class Solution:
    def NGL(self, arr):
        stack = deque()
        res = []
        for i in range(len(arr)):
            if len(stack) == 0:
                res.append(-1)
            elif arr[i] < stack[0]:
                res.append(stack[0])
            while len(stack) !=0 and arr[i] >= stack[0]:
                stack.popleft()
                if len(stack) == 0:
                    res.append(-1)
                elif arr[i] < stack[0]:
                    res.append(stack[0])
            stack.appendleft(arr[i])
        return res

arr = [2,1,4,2]       
cls_obj = Solution()
result = cls_obj.NGL(arr)
print(result)
