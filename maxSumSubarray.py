class Solution:
    def maxSumSubarray(self, arr, k):
        i = 0
        j = 0
        subarray_sum = 0
        max_sum = float('-inf')
        while j < len(arr):
            subarray_sum += arr[j]
            if j-i+1 == k:
                max_sum = max(subarray_sum, max_sum)
                subarray_sum -= arr[i]
                i += 1
            j+=1
        return max_sum

nums = [1,2,5,4,8,9,10]
solution_instance = Solution()
result = solution_instance.maxSumSubarray(nums, 3)
print("longest Sub-sequence with max sum is: ",result)
