class Solution(object):
    def twoSum(self, numbers, target):
        for i in range(0,len(numbers)):
            x=target-numbers[i]
            r=len(numbers)-1
            l=i+1
            
            while l<=r:
                m = ((r + l)// 2)
                if numbers[m] == x: 
                 return [i+1,m+1]
                if numbers[m] < x :
                 l = m + 1
                else:
                 r = m - 1 