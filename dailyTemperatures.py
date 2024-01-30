from collections import deque
class Solution:
    
    def dailyTemperatures(self, temperatures):
        stack = deque()
        res = []
        for index, value in enumerate(reversed(temperatures)):
            while len(stack) != 0 and value >= stack[0][0]:
                stack.popleft()
            if len(stack) == 0:
                res.append(0)
            elif value < stack[0][0]:
                res.append(index - stack[0][1])
            stack.appendleft([value,index])
        res.reverse()
        return res

            
# Driver Code
arr = [89,62,70,58,47,47,46,76,100,70]
cls_obj = Solution()
result = cls_obj.dailyTemperatures(arr)
print(result)
