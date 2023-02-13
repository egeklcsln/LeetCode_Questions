class Solution(object):
    def countOdds(self, low, high):
       if low%2==0 and high%2==0:
           return (high - low)/2
       return int((high - low)/2)+1