'''
2 pointer starting at sqrt of c
'''
import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, math.floor(math.sqrt(c))
        while l <= r:
            total = l**2 + r**2
            if total == c:
                return True
            elif total < c:
                l += 1
            else:
                r -=1
            
        return False
        