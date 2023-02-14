class Solution(object):
    def isSubsequence(self, s, t):
       if(len(s)==0):
           return True
       sp=0
       tp=0
       while(tp<len(t)):
           if t[tp]== s[sp]:
               sp+=1
               if sp==len(s):
                   return True



           tp+=1
            
       return False
            