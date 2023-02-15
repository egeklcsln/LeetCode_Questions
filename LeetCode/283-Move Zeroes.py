class Solution(object):
    def moveZeroes(self, nums):
         s=nums.count(0)
         for i in range(s):
          nums.remove(0)
          nums.append(0)
