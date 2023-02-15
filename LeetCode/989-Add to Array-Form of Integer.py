class Solution(object):
    def addToArrayForm(self, num, k):
        m=1
        sum=k
        list=[]
        for i in range(len(num)-1,-1,-1):
           sum +=num[i]*m
           m*=10
        
        for j in str(sum):
           list.append(int(j))
        
        return list