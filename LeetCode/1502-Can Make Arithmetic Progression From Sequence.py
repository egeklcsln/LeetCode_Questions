class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()

        for i in range(0,len(arr)-2):
            if not(arr[i+1] - arr[i])==(arr[i+2] - arr[i+1]):
                return False
        return True