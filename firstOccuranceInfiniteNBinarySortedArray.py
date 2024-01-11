class Solution:
    def infinite_binary_search(self, arr, key):
        low = 0
        high = 1
        while low <= high:
            if key > arr[high]:
                low = high
                high = high *2
            else:
                res = self.first_occurance(arr,low,high,key)
                return res

    def first_occurance(self, arr,low,high,key):
        res1 = 0
        while low <= high:
            mid = low +int((high-low)/2)
            if arr[mid] == key:
                res1 = mid
                high = mid-1
            elif arr[mid] < key:
                low = mid+1    
            else:
                high = mid-1
        return res1


# Example usage
arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
key = 1
solution_obj = Solution()
result = solution_obj.infinite_binary_search(arr, key)
print("First occurrence of", key, "is at index:", result)
