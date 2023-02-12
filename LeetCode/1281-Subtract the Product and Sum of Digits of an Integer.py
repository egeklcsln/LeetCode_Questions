class Solution(object):
    def subtractProductAndSum(self, n):
        multip=1
        sum=0
        
        for i in str(n):
            sum+=int(i)
            multip*=int(i)

        return multip - sum