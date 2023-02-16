class Solution(object):
    def areAlmostEqual(self, s1, s2):
        if s1==s2:
            return True
        
        temp=[]
        for i in range(0,len(s1)):
            if s1[i]!=s2[i]:
             temp.append(i)
            if len(temp)>2:
                return False
        
        if len(temp)==1:
            return False

        if s1[temp[0]]==s2[temp[1]] and s1[temp[1]]==s2[temp[0]]:
            return True

        

        
            
        return False