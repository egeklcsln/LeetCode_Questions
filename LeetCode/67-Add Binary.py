class Solution(object):
    def addBinary(self, a, b):
        sum= int(a,2) + int(b,2)
        return str(bin(sum)[2:])