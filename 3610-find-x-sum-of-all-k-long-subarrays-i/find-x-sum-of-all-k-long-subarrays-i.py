'''
keep count of occurences
keep heap of size x
tc nklogx
'''
import heapq
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        occ = {}
        #build of size x - 1
        for i in range(k-1):
            num = nums[i]
            if num not in occ:
                occ[num] = 0
            occ[num] += 1
        ans = []
        for i in range(k-1, len(nums)):
            num = nums[i]
            if num not in occ:
                occ[num] = 0
            occ[num] += 1
            pq = []
            for n, o in occ.items():
                heapq.heappush(pq, (o,n))
                if len(pq) > x:
                    heapq.heappop(pq)
            curr = 0
            for key, val in pq:
                curr += key*val
            ans.append(curr)

            numToRemove = nums[i - k + 1]
            occ[numToRemove] -= 1
            if occ[numToRemove] == 0:
                occ.pop(numToRemove)
        return ans

        