class Solution(object):
    def runningSum(self, nums):
        list=[]
        for i in range(0,len(nums)):
         list.append(sum(nums[0:(i+1)]))
        return list