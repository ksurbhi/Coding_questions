class Solution:
    def productExceptSelf(self, nums):
        l = 0
        r = len(nums)-1
        res = [1]*len(nums)
        left_Prod = 1
        right_Prod = 1
        while l < len(arr) and r >-1:
            res[l] = res[l] *left_Prod 
            res[r] = res[r] * right_Prod
            left_Prod = left_Prod * nums[l]
            right_Prod = right_Prod * nums[r]
            l += 1
            r -= 1
        return res

arr = [1,2,3,4]
class_obj = Solution()
res = class_obj.productExceptSelf(arr)
print(res)      
