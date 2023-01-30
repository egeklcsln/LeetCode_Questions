class Solution(object):
    def twoSum(self, nums, target):
        list = []
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if i==j:
                    continue
                sum= nums[i]+nums[j]
                if sum==target:
                    list.append(i)
                    list.append(j)
                    return list