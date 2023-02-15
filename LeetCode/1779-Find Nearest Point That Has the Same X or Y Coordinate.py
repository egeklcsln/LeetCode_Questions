class Solution(object):
    def nearestValidPoint(self, x, y, points):

        s=0
        list_a=[]
        list_s=[]
        for i in points:
            a=(abs(x-i[0]) + abs(y-i[1]))
            if a==0 and (i[0]==x or i[1]==y) :
             return s
            if (a not in list_a) and (i[0]==x or i[1]==y):
                list_a.append(a)
                list_s.append(s)
                
            s+=1

        if list_a==[]:
                return -1

        return list_s[list_a.index(min(list_a))]