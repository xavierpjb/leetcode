'''
subtract the smallest number at each point
insert all nums into a pq, subtract then repeat
'''
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        uniqNums = set(nums)
        ans = len(uniqNums)
        if 0 in uniqNums:
            ans -= 1
        return ans
                