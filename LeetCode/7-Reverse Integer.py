class Solution(object):
    def reverse(self, x):
     if x>=0:   
        a=str(x)
        a= a[::-1]
        result= int(a)
     if x<0:
        a=str(x)
        a=a[1:]
        a=a[::-1]
        result= int(a)*(-1)
     if result >(2**31 - 1) or result<((-1)*2**31):
        return 0
     return result