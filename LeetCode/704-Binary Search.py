class Solution(object):
    def search(self, nums, target):
        nums.sort()
        s=0
        for i in nums:
            if i==target:
                return s
            s+=1
        return -1