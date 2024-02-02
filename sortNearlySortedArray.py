
import heapq
class Solution:    
    def sortNearlySortedArray(self, arr, k):
        heap = []
        result = []
        for ele in arr:
            heapq.heappush(heap,ele)
            if len(heap) >k:
                result.append(heapq.heappop(heap))
        while len(heap) >0:
            result.append(heapq.heappop(heap))
        return result


# Driver Code
arr = [10, 9, 8, 7, 4, 70, 60, 50]
k = 4
cls_obj = Solution()
result = cls_obj.sortNearlySortedArray(arr, k)
print(result)
