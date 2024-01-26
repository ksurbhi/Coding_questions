from collections import deque

class Solution:
    def NGR(self, arr):
        stack = deque()
        res = []
        # import pdb; pdb.set_trace()
        for i in range(len(arr)-1, -1, -1):
            if len(stack) == 0:
                res.append(-1)
            elif arr[i] < stack[0]:
                res.append(stack[0])
            while len(stack) != 0 and arr[i] >= stack[0] :
                stack.popleft()
                if len(stack) == 0:
                    res.append(-1)
                elif arr[i] < stack[0]:
                    res.append(stack[0]) 
            stack.appendleft(arr[i])
            print(stack)
       
        res.reverse()
        return res

arr = [1,3,2,4]       
cls_obj = Solution()
result = cls_obj.NGR(arr)
print(result)
