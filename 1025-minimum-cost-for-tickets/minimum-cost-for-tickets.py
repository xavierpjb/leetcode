'''
Single source shortest path

by 1 7 or 30 day pass

src 0, dest is len(arr)

buy pass, calculate how far it gets you, add to queue
'''
import heapq
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        pq = [(0,0)]
        heapq.heapify(pq)
        visited = set()
        while True:
            cost, curr = heapq.heappop(pq)
            if curr == len(days):
                return cost
            if curr in visited:
                continue
            visited.add(curr)
            # calculate next steps
            dayOffset = 1
            heapq.heappush(pq, (cost + costs[0], curr + dayOffset))

            while curr + dayOffset < len(days) and days[curr + dayOffset] < days[curr] + 7:
                dayOffset += 1
            heapq.heappush(pq, (cost + costs[1], curr + dayOffset))
            
            while curr + dayOffset < len(days) and days[curr+dayOffset] < days[curr] + 30:
                dayOffset += 1
            heapq.heappush(pq, (cost + costs[2], curr + dayOffset))

            

        


        

