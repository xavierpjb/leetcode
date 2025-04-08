'''
Use monotonic stack
[1,3, 4, 2]
[3,4,-1,-1]
use a map to determine next greater element


[2,4]

'''
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = {num:-1 for num in nums2}

        i = 0
        stack = []

        while i < len(nums2):
            currNum = nums2[i]
            while stack and nums2[stack[-1]] <= currNum:
                iNum = stack.pop()
                ans[nums2[iNum]] = currNum
            stack.append(i)
            i += 1



        return [ans[num] for num in nums1]

        

        