'''
Problem: given 2 sorted arrays (1 indexed, non-decreasing), 
find 2 numbs that sum to target. 
There is always one solution, cannot return 2 of the same index

examples:
given to the right

scenarios:

a = [1,2,3], t = 3 -> [1,2]

ideas:
find if match exists for each element t.c = n^2, s.c = 1

find match using 2pp
0 and last, if too small, increment first, if to big , decrement last
return first+1, last

test:


'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l != r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l+1, r+1] #mistake, forgot to add one to right index as well
            if sum < target:
                l += 1
            else:
                r -= 1
'''
test
 [1,2,3] t = 3
 l^ 
 r  ^
'''
        