'''
problem: <

example
[1,2,3]
[1,3,2]
[2,1,3]

scenarios

1,1,5
[1,1,5]
[1,5,1]
[1,1,5]
[1,5,1]
[5,1,1]
[5,1,1]

possibel options for 1st 1,1,5
second possible option 
1,1,5
1,1,5
1,5,1
1,5,1
5,1,1
5,1,1

input: arr of nums
work: gen next permutation
output: inplace shifting to next permutation

ideas:
generate all possible permutation until then generate one more
n!

[1,2,3,4]
[4,3,2,1]

[1,2,3,4]
[1,2,4,3]
[1,3,2,4]
[1,3,4,2]
[1,4,2,3]
[1,4,3,2]
[
[2,4,3,1]
[3,1,2,4]

[1,2,4,3]
[1,3,2,4]
[1,3,4,2]
[1,2]
[2,1] push smaller number back
[3,1]
[1,3] swap l and r
[1,2,3]
[1,3,2]
if it's not in descending order, then there is a permuation that isn't a reversal

[3,2,1]

[5,3,2,4]

[2,1,4,3]
[2,3,1,4]
[2,3,1,2,2,4]
[4,1,2,3]

[2,]

[1,2,3,4]
[1,2,2]
[2,2]
[]
[1,3,2,4]
[1,3,4,2]
[1,4,2,3]
[2,4,3,1]
[2,1,3,4]
[2,]

starting from right, find first number that breaks ascending order sequce
if no number found, reverse
if a number is found
look for last number bigger than number to swap
then revers up to that index and return arr



'''

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        def rev(l,r):
            while l < r:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l+=1
                r -= 1

        r = len(nums) - 2

        while r >= 0 and nums[r] >= nums[r+1]: #infinite loop
            r -= 1
        if r < 0:
            rev(0, len(nums) - 1)
            return
        #find first bigger number than r
        other = len(nums) - 1
        while nums[r] >= nums[other]:
            other -= 1
        
        temp = nums[other]
        nums[other] = nums[r]
        nums[r] = temp
        rev(r+1,len(nums) - 1)
        '''
        2,2,3
       r^
       o    ^
       temp = 3
       3,2,2
       r
         o

        '''
        

        
        #find first number bigger
        
    
        