'''
idea
brute for
for every window of size k, look for max
tc = O(k*n)

optimized? n

way to remove and add
if you encounter a number bigger than the max, update max

if max is out of window, find next max
maybe pq? nlogn

when element removed, it can be any number between k


idea

start with a pq of size k
set the first answer to the first element

iterate through rest of list by adding i + (k - 1)

k = 1

solution

using a pq, lefmost element will be the max
anything while appendiing the queue, remove anything that you're bigger than
fill the deque up to k with value and index
'''
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        class Elem:
            def __init__(self, val, index):
                self.val = val
                self.i = index
        dq = deque()
        for i in range(k - 1):
            while dq and dq[-1].val < nums[i]:
                dq.pop()
            dq.append(Elem(nums[i], i))
        
        ans = []
        for i in range(len(nums) - k + 1):
            iNext = i + k - 1
            while dq and dq[-1].val < nums[iNext]:
                dq.pop()
            dq.append(Elem(nums[iNext], iNext))

            ans.append(dq[0].val)
            if dq[0].i == i :
                dq.popleft()
            
        '''
        [1,3,-1,-3,5,3,6,7] k = 3
        i(0,6) i = 3
        dq[(5,4)(3,5)]
        ans[3,3,5,5]
        iNext = 5




        '''
        return ans


        



        

        