'''
Problem: given an array of numbers, find all triplets of diff indexes such that they add up to 0. solution must not contain duplicate triplets

examples: <<

scenarios:

0, 1, 2, -1 -> 0, 1, -1

input: list of numbers (unsorted)
work: find triplets that sum to 0
output: the numbers that sum to 0, no dup entry

ideas:

brute force: generate all arrays of size 3, put in set and validate answer not in list
t.c = n*n*n
s.c = n

optmized:
sort array
for every number x, find 2 sum that adds up to x * -1
t.c = n*n = n^2
s.c = n (sorting and solution)

handling duplicates -> move array till new number found (since array is sorted)
terminate when l = r (inner loop)
terminate when l - len(arr) <= 2

tests

-1, 0, 1, 1, 1



'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # find all threesum
        nums.sort()
        threeSum = ThreeSum(nums)
        l = 0
        while len(nums) - l > 2:
            threeSum.find(nums[l], l+1)
            while l + 1 < len(nums) and nums[l] == nums[l+1]: #off by one error
                l += 1
            l += 1
        return threeSum.solutions



class ThreeSum:
    def __init__(self, nums):
        self.nums = nums
        self.solutions = []

    def find(self, firstNum, startIndex):
        #from start index to end of array,
        target = -1 * firstNum
        #unitiliazed l and r
        l, r = startIndex, len(self.nums) - 1 #wrong start index (started at 0)
        while l < r:
            if self.nums[l] + self.nums[r] == target:
                self.solutions.append([firstNum, self.nums[l], self.nums[r]])#syntax error, forgot bracket and self at start
                while l + 1 < len(self.nums) and self.nums[l] == self.nums[l+1]:
                    l += 1
                l+=1
                while r - 1 > 0 and self.nums[r-1] == self.nums[r]:
                    r -= 1
                r-=1
            elif self.nums[l] + self.nums[r] > target:
                while r - 1 > 0 and self.nums[r-1] == self.nums[r]:
                    r -= 1
                r -= 1
            else:
                while l + 1 < len(self.nums) and self.nums[l] == self.nums[l+1]:
                    l += 1
                l += 1

'''
did not handle dups
'''

