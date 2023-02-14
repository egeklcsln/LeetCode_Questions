class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s)!=len(t):
            return False

        list1=[]
        list1LT=[]
        list2=[]
        list2LT=[]
        a=0
        b=0
        for i in range(0,len(s)):
         if not s[i] in list1LT:
             list1LT.append(s[i])
             list1.append(a)
             a+=1
         if s[i] in list1LT:
             ind = list1LT.index(s[i])
             list1.append(ind)

        
         if not t[i] in list2LT:
             list2LT.append(t[i])
             list2.append(b)
             b+=1
         if t[i] in list2LT:
             ind = list2LT.index(t[i])
             list2.append(ind)


        if list1==list2:
            return True
        return False
