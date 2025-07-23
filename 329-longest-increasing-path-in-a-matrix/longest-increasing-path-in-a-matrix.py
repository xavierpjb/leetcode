'''
ideas

set longest increasing path as you traverse

outline

for m*n matrix, set longest path to -1 (also unvisited)
for ever node, pick max between up down left and right
'''
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        g = Graph(matrix)
        return g.longest


class Graph:
    def __init__(self, matrix):
        self.matrix = matrix
        self.y = len(matrix)
        self.x = len(matrix[0]) 
        self.paths = [[-1 for _ in range(self.x)] for _ in range(self.y) ] #problem with instantiation
        self.longest = -1
        for y in range(self.y):
            for x in range(self.x):
                self.findLength(x,y, -1)

    def findLength(self, x, y, parent):
        if x < 0 or x == self.x:
            return 0
        if y < 0 or y == self.y:
            return 0
        if parent >= self.matrix[y][x]:
            return 0
        if self.paths[y][x] != -1:
            return self.paths[y][x]
        maxLen = 0
        for direction in self.getDirections(x,y):
            maxLen = max(maxLen, self.findLength(direction[0], direction[1], self.matrix[y][x]))
        maxLen += 1
        self.paths[y][x] = maxLen
        self.longest = max(maxLen, self.longest)
        return maxLen
        
        
    def getDirections(self, x, y):
        return[[x+1, y],[x-1,y],[x,y+1],[x,y-1]]





