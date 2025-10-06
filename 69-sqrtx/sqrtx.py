class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l < r:
            mid = (l + r)// 2
            if self.isPossible(mid, x):
                r = mid
            else:
                l = mid + 1
        if l*l == x:
            return l
        return l - 1
        
    def isPossible(self,mid, x):
        return mid * mid >= x
        