class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        sol = nums[l] + nums[r]
        l+=1
        r-=1
        while l < r:
            sol = max(sol, nums[l] + nums[r])
            l+=1
            r-=1
        return sol

        
        