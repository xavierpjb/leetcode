'''
choose the path with the smallest increase in maxeffort
'''
import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        #initialize and array of positive inf
        self.xLim, self.yLim = len(heights), len(heights[0])
        #efforts = [[float("inf") for _ in range(self.yLim)] for _ in range(self.xLim)]
        #efforts[0][0] = 0
        pq = [(0,(0,0))]
        visited = set()
        while pq:
            effort, coord = heapq.heappop(pq)
            if coord[0] == self.xLim - 1 and coord[1] == self.yLim - 1:
                return effort
            if coord in visited:
                continue
            visited.add(coord)
            for move in self.nextMoves(coord):
                if move not in visited:
                    currEffort = max(effort, abs(heights[coord[0]][coord[1]] - heights[move[0]][move[1]]))
                    heapq.heappush(pq, (currEffort, move))


    def nextMoves(self, coord):
        ans = []
        x, y = coord
        if x - 1 >= 0:
            ans.append((x-1,y))
        if y - 1 >= 0:
            ans.append((x, y-1))
        if x + 1 < self.xLim:
            ans.append((x+1, y))
        if y + 1 < self.yLim:
            ans.append((x, y+1))
        return ans

        