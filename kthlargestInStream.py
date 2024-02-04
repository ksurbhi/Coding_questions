import heapq
class KthLargest:

    def __init__(self, k, arr):
        # Initialize the KthLargest object with k and min_heap
        self.k = k
        self.min_heap = arr
        heapq.heapify(self.min_heap)
        # Ensure the heap has only k elements
        while len(self.min_heap) >self.k:
            heapq.heappop(self.min_heap)
    
    def add(self, val):
        # Add the new value to the heap
        heapq.heappush(self.min_heap, val)
         # Ensure the heap has only k elements
        while len(self.min_heap) >self.k:
            heapq.heappop(self.min_heap)
         # Return the current kth largest element
        return self.min_heap[0]
    
# Driver code
obj = KthLargest(3, [4, 5, 8, 2])
param_1 = obj.add(4)
print(param_1)
param_1 = obj.add(5)
print(param_1)
param_1 = obj.add(5)
print(param_1)
param_1 = obj.add(8)
print(param_1)
param_1 = obj.add(8)
print(param_1)
