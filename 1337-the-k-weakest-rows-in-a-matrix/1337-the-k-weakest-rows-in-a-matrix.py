'''
13
problem:
    given m*n matrix of 1s and 0s. 1 are in from of 0, (all 1 will appear left of 0s in each row)
    i weaker than j if:
        num 1s in i < num 1 in j
        num 1s in i == num 1s in j and i < j
    return k weakest rows

input:
    mat: m*n matrix of 1 and 0s
    k: the k rows to return
work:
    find the k weakest rows
output:
    int[]: k weakest rows from weakest to strongest
    
examples:
    given in prompt
    
ideas:
    find the last 1: linear = O(n), binsearch = O(logn)
    keep a heap of size k and update as we calculate weaknesses (strongest on top)
        don't replace max heap when current elem.strength == top of heap strength
test:
    varying weaknesses
        equivalent weakness lower index
        
        weaker

no need to check for k since k <= m
'''
import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        #while were not done with the list, find last 1
        # check if element should be added to heap
        pq = []
        #store the strength negatively since its a min heap
        R = len(mat)
        C = len(mat[0])
        def findS(row):
            l, r = -1, C-1 #bug, did not choose proper end criteria
            while l < r:
                mid = ceil((l+r)/2)
                if row[mid]:
                    l = mid
                else:
                    r = mid - 1
            return l + 1
            
        for i, row in enumerate(mat):
            strength = findS(row)
            heapq.heappush(pq, (-strength, -i))
            if len(pq) > k:
                heapq.heappop(pq)
        sol = [-(heapq.heappop(pq)[1]) for i in range(len(pq))]
        sol.reverse()
        return sol
            
        