class Solution(object):
    def search(self, nums, ele):
        """
        :type nums: List[int]
        :type ele: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = int((start + end) /2)
            if ele == nums[mid]:
                return mid
            elif ele > nums[mid]:
                start = mid+1
            else:
                end = mid - 1
        return -1

    
    ##########################################################
    ############# when array is in decending order ###########
    def binary_search_decending_order_array(self, nums, ele):
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = int((start + end) /2)
            if ele == nums[mid]:
                return mid
            elif  nums[mid] > ele:
                start = mid+1
            else:
                end = mid - 1
        return -1


    ##########################################################
    ############# when order of the array is not known #######
    
    def unorded_search(self, nums, ele):
        start = 0
        end = len(nums) - 1
        if nums[start] < nums[start+1]:
            self.search(nums, ele)
        elif nums[start] > nums[start+1]:
            self.binary_search_decending_order_array(self, nums, ele)
            





        
        
    
