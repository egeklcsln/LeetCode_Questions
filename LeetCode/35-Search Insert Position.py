class Solution(object):
    def searchInsert(self, nums, target):
        s=0
        for i in nums:
         if i==target:
             return s
         if i>target:
             break
         s+=1

        return s