'''
problem: < return kth largest element
examples
scenarios
[1] return elem
[2,1] k = 1 return 2, k=2 return 1

input: list of nums
work: find kth largest
output: kth larget

ideas:
sort then return at index k
nlogn space and time

keep a heap of k largest elements
k space, nlgn time
if larger than smallest remove 
if smaller than smallest, ignore





'''
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #fill heap up to k
        kElems = [nums[x] for x in range(k)]
        heapq.heapify(kElems)
        for x in range(k, len(nums)):
            heapq.heappushpop(kElems, nums[x])

        return kElems[0]



        