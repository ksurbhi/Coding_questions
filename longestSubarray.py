class Solution:
    def longestSubarray(self, arr, k):
        i = 0
        sum = 0
        max_len = -1
        for j in range(len(arr)):
            sum = sum +arr[j]
            if sum == k:
                max_len = max(max_len, j-i+1)
            elif sum >k:
                while sum >k:
                    sum = sum -arr[i]
                    i += 1
        return max_len

nums = [1]
solution_instance = Solution()
result = solution_instance.longestSubarray(nums, 1)
print("lengest subarray of size k: ", result)
