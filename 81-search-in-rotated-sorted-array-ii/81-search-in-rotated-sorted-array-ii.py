'''
13
problem:
    given an array (nums) of non-decreasing ints,  and an int (target), return true if target is in num, false other
    note: array is rotated such that at some point k, we loop back to the beginning for increasing order
    decrease operations steps as much as possible
input:
    nums: int[] rotated at pivot k (k unknown)
    target: int number to find if it exists
work:
    go through the array and return wether the number exists
return:
    boolean: number exists?

examples:
    given in prompt (number contained and number not contained)
    
ideas:
    bf:
        go through the array linearly and search for element occurent
        t = O(n)
        s = O(1)
    divide the list:
        look for sorted and not sorted subsections
        t = O(logn)
test:
    number in list
    
    number not in list
Super massive logic bug, did not account for list in increasing order with duplicates
'''
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # if withing the subset that's sorted go there, else go to the other half and looks again
        return target in nums
        