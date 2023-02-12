class Solution(object):
    def countBits(self, n):
        list=[]
        s=0
        for i in range(n+1):
           s=0
           a= bin(i)[2:]
           for j in a:
               if j=="1":
                   s+=1
           list.append(s)
               
           

        return list