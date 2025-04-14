'''
problem: <
examples: <

scenarios:

[0] -> 0
[1,1,0,2] -> 2

input: list of heights
work: find the max area
output: max

ideas:

brute force:
for every bar, calculate area with next bar
Time O(n^2) space = O(1)

generate next smaller element from left and right for each index
(r-1) - (left+1) + 1  will be the r-1-l-1+1 =  r-l-1
get the max



'''

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #next smallert elem ltr
        nxSmallerLtr = [-1] * len(heights)
        stack = []

        for i, val in enumerate(heights):
            while stack and heights[stack[-1]] > val:
                stackElem = stack.pop()
                nxSmallerLtr[stackElem] = i
            stack.append(i)
            #[1,2,3]
            # nx = 1,-1,4,4
        
        #next smaller element rtl
        nxSmallerRtl = [-1] * len(heights)
        stack = []
        for i in range(len(heights)-1, -1, -1):
            val = heights[i]
            while stack and heights[stack[-1]] > val:
                stackElem = stack.pop()
                nxSmallerRtl[stackElem] = i
            stack.append(i)

        #for every element, get both indexes and calculate area, return max area
        area = 0
        for i, val in enumerate(heights):
            l = nxSmallerRtl[i]
            r = nxSmallerLtr[i] if nxSmallerLtr[i] != -1 else len(heights)
            area = max(val*(r-l-1), area)

        return area

        