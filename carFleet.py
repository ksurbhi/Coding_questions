from collections import deque
class Solution:
    def carFleet(self, position, speed,target):
        car_prop = list(zip(position, speed))
        car_prop.sort(reverse = True)
        stack = deque()
        for (p,s) in car_prop:
            time = (target - p)/s
            if len(stack) ==0:               
                stack.appendleft(time)
            else:
                if time > stack[0]:
                    stack.appendleft(time)
        return len(stack)

            
# Driver Code
target = 10
position = [0,2,4]
speed = [4,2,1]
cls_obj = Solution()
result = cls_obj.carFleet(position, speed,target)
print(result)
