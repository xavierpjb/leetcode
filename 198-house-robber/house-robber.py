'''
break into 1 or 2 then pick max from 1 or 2

100, 9, 1, 100
1,9,100

pick 0, 1 or 2

f(n) = max(
    f(n+3),// pick 0 elems
     nums[n]+f(n+2), // pick first f1 then break go to next house
     f(n+1), // pick second elem
     )

f(0) = max(f(3))

start with last 3 elems
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        a, b = nums[0], nums[1]
        c = a + nums[2]

        for x in range(3,len(nums)):
            curr = nums[x]
            newC = max(a + curr, b + curr, c)
            a, b, c = b, c, newC
        
        return max(a,b,c)


        