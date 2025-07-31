'''
Dijksta keeping track of number of stops, we reach dst within k stops that's the cheapest, otherwise explore alternatives
'''
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = Graph(flights, n)
        return g.findCheapestWithingK(src, dst, k)


class Graph:
    def __init__(self, flights, n):
        self.graph = {i:[] for i in range(n)}
        self.buildGraph(flights)

    def buildGraph(self, flights):
        for fr, to, price in flights:
            self.graph[fr].append(Connection(to,price, -1))

    def findCheapestWithingK(self, src, dst, k):
        q = [Connection(src, 0, -1)]
        visited = set()
        stopsWhenVisited = [float("inf")] * len(self.graph)
        while q:
            curr = heapq.heappop(q)
            if curr.stops > k:
                continue
            if curr.city == dst:
                return curr.price
            if curr.city in visited and curr.stops >= stopsWhenVisited[curr.city]: #mistake > instead of =
                continue
            visited.add(curr.city) #did not add to visited
            stopsWhenVisited[curr.city] = curr.stops
            for nei in self.graph[curr.city]:
                heapq.heappush(q, Connection(nei.city, nei.price + curr.price, curr.stops + 1))

        return -1

        

class Connection:
    def __init__(self, city, price, stops):
        self.city = city
        self.price = price
        self.stops = stops

    def __lt__(self, other):
        if self.price != other.price:
            return self.price < other.price
        
        return self.stops < other.stops


        