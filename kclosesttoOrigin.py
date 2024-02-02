import heapq
from math import sqrt
class Solution:   
    def Closest_to_Origin(arr,list,k): # closest means smallest ---> Max heap
        heap = []
        for ele in list:
            dist = -sqrt((ele[0] ** 2) + (ele[1] ** 2))
            heapq.heappush(heap, (dist, ele))
            if len(heap) > k:
                heapq.heappop(heap)
        return [val[1] for val in heap]






# Driver Code
points = [[3,3],[5,-1],[-2,4]]
k = 2
cls_obj = Solution()
result = cls_obj.Closest_to_Origin(points, k)
print(result)
