class MinimumInRotatedSortedArray:

    def __init__(self, arr):
        self.arr = arr

    def search(self):
        # Initialize pointers for binary search
        low =0
        n = len(self.arr)
        # Initialize the minimum element to positive infinity
        min_ele = float('inf')
        high = n-1
        # Perform binary search
        while low <= high:
            mid = int(low +(high -low)/2)
            # Check if the left part is sorted
            if self.arr[low] <= self.arr[mid]:
                # Update the minimum element and move to the right
                min_ele = min(self.arr[low],min_ele)
                low = mid + 1
            else:
                # Update the minimum element and move to the left
                min_ele = min(self.arr[mid], min_ele)
                high = mid-1
        # Return the minimum element found
        return min_ele

arr = [4,5,6,7,0,1,2]
obj1 = MinimumInRotatedSortedArray(arr)
res = obj1.search()
print("Minimum element in rotated sorted array",res)



arr = [4, 5, 6, 1, 2, 3]
target = 3 #0, 10, 4, 3
object_of_class = RotatedArray(arr, target)
res = object_of_class.search()
print(res)

