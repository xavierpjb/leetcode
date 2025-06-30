'''
problem: return the kth smallest fraction
examples:

scenarios:

[1,2,3] 

1/2, 1/3, 2/3
1/3, 1/2, 2/3

input: list of prime nums
work find kth smallest fraction
output: return kth smallest fraction

ideas:
generate all possible fractions (n2), keep a heap of size k, return top of heap

numerator/denominator

2 pointer?

next consideration
left div, right div
num[0]/nums[end] < nums[1]/nums[end]?

for k interations
if left < right, find next for left
if right < left set 

store top number over biggest denom
k log n

stored equations and indexes

(n+(k-n)) log n


'''
import heapq
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        class Frac:
            def __init__(self, num, den, iDen):
                self.num = num
                self.den = den
                self.iDen = iDen

            def __lt__(self, other):
                return (self.num /self.den) < (other.num /other.den)

            def hasNext(self):
                return arr[self.iDen] != self.num

            def next(self):
                self.iDen -= 1
                self.den = arr[self.iDen]
        pq = []
        end = len(arr) - 1
        for i in range(len(arr) - 1):
            pq.append(Frac(arr[i], arr[end], end))
        heapq.heapify(pq)

        # if len(pq) <= k:
        #     for _ in range(k-1):
        #         heapq.heappop(pq)
        #     ans = pq[0]
        #     return [ans.num, ans.den]
        
        for _ in range(k-1):
            smallest = heapq.heappop(pq)
            if smallest.hasNext():
                smallest.next()
                heapq.heappush(pq, smallest)
        ans = pq[0]
        return [ans.num, ans.den]
        