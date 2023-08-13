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
