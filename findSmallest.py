import heapq
class Solution:
  def kthSmallestElement(self, arr, k):
          heap = []
          for i in range(len(arr)):
              heapq.heappush(heap, -arr[i])
              if len(heap) > k:
                  heapq.heappop(heap)
          return -heap[0]


# Driver Code
nums = [3,2,3,1,2,4,5,5,6]
k = 3
cls_obj = Solution()
result = cls_obj.kthSmallestElement(nums,k)
print(result)
