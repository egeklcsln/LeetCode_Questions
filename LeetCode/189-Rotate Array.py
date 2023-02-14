class Solution(object):
    def rotate(self, nums, k):
        if len(nums)==1:
            return
        if len(nums)==2:
            if k%2==0:
                return
            temp=nums[0]
            nums[0]=nums[1]
            nums[1]=temp
            return

        temp1=nums[(len(nums)-k):]
        temp2=nums[:(len(nums)-k)]
        nums[:]= temp1 + temp2