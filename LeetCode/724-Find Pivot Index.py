class Solution(object):
    def pivotIndex(self, nums):
       total = sum(nums)
       lSum=0
       for i in range(len(nums)):
           rSum= total - lSum - nums[i]
           if lSum == rSum:
               return i
           lSum+=nums[i]
       return -1       
