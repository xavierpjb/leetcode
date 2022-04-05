'''
Given an array of int where vali reps height of pole at i
maximize val(min(i,j)) * j - 1
Contraints:
we get at least 2 poles
poles vary from 0 to 10000
input:
  height: array of int
output:
  maximum area


[1,8,5,8]
min(a[i], a[j])* i - j for every pole, then return global max

divid and conquer
max area left, max area right, max area mid, return max of all

linear
[1,2,1]
global max = 1

local_max = max(getArea(i,j), getArea(j-1,j))
if global


getArea
min(a[i], a[j])* i - j
i = 0
j = 1
gmax = getArea(ij)
from j+1 to eoa:
  if getArea(i,)
you could eithre be super long, or super tall
either
is there a way in constant time to tell the max area of a pole?
farthest pole with height >= self
[1,2,1,3]
 ---1
 -----2
   ---1
   
if its 1, max area is fartest pole with height 1
it its 2, max area is farthest pole with height >= 2
the only pole that wouldnt have a height > is max pole
the smaller poles would be able to find the bigger poles
X

2 pp
max area with base of len(arr) is the one with the lowest hight,
when proceeding, choose the bigger of the two possible bars

what if we up

outline:
while left < right
global area = max(global_area, getArea(ij))
if a[l+1] > a[r-1], l+=1, else right -=1
update whatever is smallest

1,2,1,4,3], drop the lowest pole at each iteration
[233]
21413
[1]
we want to get rid of the smallest of the 4 valu
43
3 (3*1)
2*2
3*1
if l < r
  if l <= l+1: 
    l+=1
  if l+1 <= r-1: l+=1
  
[1243]
[2413]
[9139]
[1213] [2]
 
   
return global area
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        glob_a = 0
        while l < r:
            glob_a = max(glob_a, getArea(height,l,r))
            if height[l] > height[r]:
                r-=1
            elif height[l] < height[r]:
                #update the smaller of the two
                l+=1
            else:
                if height[l+1]>height[r-1]:
                    l+=1
                else:
                    r-=1
        return glob_a
            
            
def getArea(a, l,r):
    return min(a[l],a[r]) * (r - l)