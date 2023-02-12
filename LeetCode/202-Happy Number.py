class Solution(object):
    def isHappy(self, n):
        s=0

        while s<100:
            sum=0
            s+=1
            for i in str(n):
                sum += (int(i)**2)

            if sum==1:
                return True
            n=sum
            
        return False