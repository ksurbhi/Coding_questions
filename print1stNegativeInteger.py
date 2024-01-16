class Solution:
    def print1stNegativeInteger(self,arr,k):
        i = 0
        j = 0
        res = []
        queue = deque()
        while j < len(arr):
            if arr[j] < 0:
                queue.append(arr[j])
            if j-i+1 == k:
                if len(queue) == 0:
                    res.append(0)
                else:
                    res.append(queue[0])
                    if arr[i] == queue[0]:
                        queue.popleft() 
                i +=1 
            j += 1
        return res

arr = [1, -2, 3, -10, 12, 13, 14]
solution_instance = Solution()
res = solution_instance.print1stNegativeInteger(arr, 3)
print(res)
