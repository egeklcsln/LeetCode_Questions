class Solution(object):
    def reverseWords(self, s):
      a=s.split()
      new_s=""
      for i in range (len(a)):
          a[i]= a[i][::-1]
          new_s=new_s+a[i]+" "

      return new_s.strip()