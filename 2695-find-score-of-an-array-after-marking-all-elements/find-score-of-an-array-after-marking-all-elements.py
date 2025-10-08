import heapq
class Solution:
    def findScore(self, nums: List[int]) -> int:
        marked = [False]* len(nums)
        pq = []
        for i, num in enumerate(nums):
            heapq.heappush(pq, (num, i))
        score = 0
        while pq:
            num, i = heapq.heappop(pq)
            if marked[i]:
                continue
            score += num
            if i - 1 >= 0:
                marked[i-1] = True
            if i+1 < len(nums):
                marked[i + 1] = True
        return score

        