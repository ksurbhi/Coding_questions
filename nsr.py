from collections import deque
class Solution:
    def NSR(self, arr):
        stack = deque()
        res = []
        # import pdb; pdb.set_trace()
        for i in range(len(arr)-1, -1, -1):
            if len(stack) ==0:
                res.append(-1)
            elif arr[i] > stack[0]:
                res.append(stack[0])
            while len(stack) !=0 and arr[i] <= stack[0]:
                stack.popleft()
                if len(stack) ==0:
                    res.append(-1)
                elif arr[i] > stack[0]:
                    res.append(stack[0])
            stack.appendleft(arr[i])
        res.reverse()
        return res


arr = [2,1,4,2]       
cls_obj = Solution()
result = cls_obj.NSR(arr)
print(result)
