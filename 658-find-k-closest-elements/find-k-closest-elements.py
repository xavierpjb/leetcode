'''
ideas

brute force would be to calc all min dist and return 4 smalles

1,2,3,4,5,6,7

find number with smallest distance than branch out, prioritizing left

'''
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k == len(arr):
            return arr
        
        #find index of smallest distance
        iSmallest = 0
        for i in range(len(arr)):
            if abs(arr[iSmallest] - x) > abs(arr[i] - x) and arr[iSmallest] != arr[i]:
                iSmallest = i
        l, r = iSmallest - 1, iSmallest + 1

        while l >= 0 and r < len(arr) and r - l - 1 < k:
            if abs(arr[l] - x) <= abs(arr[r] - x):
                l -= 1
            else:
                r += 1
        if l < 0:
            r = k
        elif r == len(arr):
            l = len(arr) - k - 1


        return arr[l+1:r]
        

        