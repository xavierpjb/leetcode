'''
l, r
anytime a 1 is encountered skip
[0,0,1,1,2,2]
     l
       i
       r

'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1

        i = 0
        while i <= r:
            num = nums[i]
            if nums[i] == 0:
                nums[l],nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
            else:
                i += 1
        return nums
        
        
        