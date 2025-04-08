'''
Use monotonic stack
[1,3, 4, 2]
[3,4,-1,-1]
use a map to determine next greater element


[2,4]

'''
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = {num:-1 for num in nums1}
        stack = []

        for i, num in enumerate(nums2):
            while stack and nums2[stack[-1]] <= num:
                ansNum = nums2[stack.pop()]
                if ansNum in ans:
                    ans[ansNum] = num
            stack.append(i)

        return [ans[num] for num in nums1]

        

        