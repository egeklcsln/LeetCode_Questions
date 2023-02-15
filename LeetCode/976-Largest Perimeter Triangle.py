class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort()
        for i in range(len(nums)-1,1,-1):
            a=nums[i]
            b=nums[i-1]
            c=nums[i-2]
            if a+b>c and a+c>b and b+c>a:
                return a+b+c
            
        return 0
        

        