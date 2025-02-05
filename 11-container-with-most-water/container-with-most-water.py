'''
Problem: <

example: <

scenarios


ideas: base biggest when distance between the two is maximal

prefer moving the smaller of the 2

tc: n
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1 # off by 1
        sol = 0

        while l < r:
            lheight = height[l]
            rheight = height[r]
            area = (r - l) * min(lheight,rheight)
            sol = max(area, sol)
            if lheight < rheight:
                l+=1
            elif lheight > rheight:
                r-=1
            else:
                if height[l+1] > height[r-1]:
                    l+=1
                else:
                    r-=1
        return sol

'''
[1,8,6,2,1]
 0 1 2 3 4
   l   r
 lheight = 1, rheight = 1, sol = 4
 area = 1 * 3 = 3


'''
        