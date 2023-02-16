class Solution(object):
    def arraySign(self, nums):

        if 0 in nums:
            return 0
        nums.sort()
        s=0
        for i in nums:
            if i>0:
                break
            s+=1
        if s%2==1:
            return -1
        return 1