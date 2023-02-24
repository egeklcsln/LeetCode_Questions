import sys
class Solution(object):
    def maxProfit(self, prices):
       minimum =sys.maxint
       maximum=0

       for i in range(len(prices)):
           if prices[i]<minimum:
               minimum=prices[i]
           elif prices[i] - minimum > maximum:
              maximum =  prices[i] - minimum

       return maximum 