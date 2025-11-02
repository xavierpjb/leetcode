'''

'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #turn into set then see if sizes match
        u = set(nums)
        return not len(u) == len(nums)
        