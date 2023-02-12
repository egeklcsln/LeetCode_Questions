class Solution(object):
    def countKDifference(self, nums, k):
        result=0
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if abs(nums[j]-nums[i])==k:
                    result+=1

        return result