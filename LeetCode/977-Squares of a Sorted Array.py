class Solution(object):
    def sortedSquares(self, nums):
        list=[i**2 for i in nums]
        list.sort()
        return list