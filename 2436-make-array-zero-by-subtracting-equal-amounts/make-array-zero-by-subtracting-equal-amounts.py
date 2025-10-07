'''
subtract the smallest number at each point
insert all nums into a pq, subtract then repeat
'''
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        uniqNums = set(nums)
        numZ = 0
        for num in nums:
            if num == 0:
                numZ += 1

        if len(nums) == numZ:
            return 0

        ans = len(uniqNums)
        if 0 in uniqNums:
            ans -= 1
        return ans
                