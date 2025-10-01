'''
for every leaf to 0, calculate amount of gas
from root

perform dfs

calculate out to cap is same as cap to out

num people, fuel cosumed, traveling cars = ceil(numPeople/seats)

base case
1, 1 

rec
if there are available seat
2,

fuel consumed = currfuel + traveling

perform topological traversal







'''
import math
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        if not roads:
            return 0
        graph = {}

        for a,b in roads:
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append(b)
            graph[b].append(a)

        fuelCost = 0
        for city in graph[0]:
            _, f = self.findAns(graph, city, set([0]), seats)
            fuelCost += f
        return fuelCost
    
    def findAns(self, graph, node, visited, seats):
        if node in visited:
            return (0, 0)
        visited.add(node)
        currFuel = 0
        currReps = 0
        for city in graph[node]:
            r, f = self.findAns(graph, city, visited, seats)
            currFuel += f
            currReps += r
        currReps += 1
        currFuel += math.ceil(currReps/seats)
        return (currReps, currFuel)

        
        

        