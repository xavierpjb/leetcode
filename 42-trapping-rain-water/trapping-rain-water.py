'''
problem: <-

examples: <-

scenarios:
at least 1 number
n < 3 returns 0
[1,0,1]
1
[2,0,2]
2
[1,0,2],[2,0,1]
1
[3,2,1,2,3]
look for heights between  where it's possible to have water

when possible to have water?
when surrounded by bigger walls
water[i] = min(l,r) - heigh[i]
need down and up
calculate valeys

l.height is start, r.height has to be <= l.height
biggest height <= l.height

[4,1,2,1,3] -> 0,4
 0 1 2 3 4
[4,1,3,1,2] -> (0,2), (2,4)
 0 1 2 3 4


if you encounter a down up bigger than you, yall form a valey
if you don't encount a down up bigger than you, the biggest down up is the valey
 biggest down up smaller than you

if you ever reach >= l.height, that's a trap
otherwise
if you  don't go down then up, invalid
if you go down then up, then return the index of the furthest up <= l.height


'''
class Solution:
    def trap(self, height: List[int]) -> int:
        sols = 0
        #find first left
        l = 0
        
        while l < len(height) - 2:
            if height[l] <= height[l+1]:
                l += 1
            else:
                r = l+1
                #while we keep going down or straight
                while r+1 < len(height) and height[r] >= height[r+1]:
                    r += 1
                r += 1
                #if last element, no way to go up
                if r == len(height):
                    return sols
                end = r
                '''
                 while r < len(height): and height[l] >= height[r]:
                    if height[end] <= height[r]:
                        end = r
                    r+=1
                '''
                while r < len(height):
                    if height[l] < height[r]:
                        end = r
                        break
                    elif height[end] <= height[r]:
                        end = r
                    r+=1
                for i in range(l,end+1):
                    sols += max(min(height[l],height[end]) - height[i],0)
                l = end
                    
        return sols