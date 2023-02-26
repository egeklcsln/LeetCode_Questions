class Solution(object):
    def longestPalindrome(self, s):
        if len(s)==1:
            return 1
       



        res = s
        sT=""
        r=0
        

        for i in range(0,len(res)):
            if res.count(res[i])>1 and (res[i] not in sT) :
                r+=int(res.count(res[i])/2)
                sT+=s[i]
        

        if r*2==len(s):
            return r*2 
        return r*2+1