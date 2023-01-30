class Solution(object):
    def isPalindrome(self, x):
        Pcontrol=False
        if x<0:
            return Pcontrol
        a = len(str(x))
        if a==1:
            return True
        
        for i in range(0,int(a/2)):
            if int(x/(10**i))%10 == int(x/10**(a-1-i))%10:
                Pcontrol=True
            else:
                Pcontrol=False
                break

        return Pcontrol
        


               

                