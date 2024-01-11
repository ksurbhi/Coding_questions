class Solution:
    def infinite_binary_search(self, arr, key):
        low = 0
        high = 1
        while low <= high:
            if arr[high] < key:
                high *= 2
            else:
                res = self.binary_search(arr, low, high, key)
                return res

    def binary_search(self, arr, low, high, key):
        while low <= high:
            mid = low + int((high - low) / 2)
            if arr[mid] == key:
                return mid
            elif arr[mid] > key:
                high = mid - 1
            else:
                low = mid + 1
        return -1

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
key = 0

class_obj = Solution()
result = class_obj.infinite_binary_search(arr, key)

if result != -1:
    print(f"Element {key} found at index {result}")
else:
    print(f"Element {key} not found")
