'''
Problem:
  input:
    edges: int[int[]] #pairs of connections
  work:
    root at 1
    find the depth of the tree
    assign each edge 1 or 2
    height of tree
    _ _ _
    1 or 2
    how to create an odd number

    e + e = e
    e + o = o
    o + o = e

    number of of at branch = number of 

    2^height(tree)
    _ => o = 1, e = 1
    _ _ => o = 1, e =  2
    _ _ _
    odd number of odds
    permutations with an odd number of odds
    n(1) = o
    n(2) = o,e e,o
    n(3) = o,e,e e,o,e e,e,o o,o,o
    return 2^ height of tree

'''
from collections import deque
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        g = self.buildGraph(edges)

        height = self.findHeight(g)
        return 2**(height-1) % (10**9 + 7)

        
    def buildGraph(self, edges):
        graph = {}
        for i, j in edges:
            if i not in graph:
                graph[i] = []
            if j not in graph:
                graph[j] = []
            graph[i].append(j)
            graph[j].append(i)
        return graph
    
    def findHeight(self, graph):
        #start trav at 1
        q = deque([1])
        h = 0
        size = 1
        visited = set()
        while q:
            curr = q.popleft()
            if curr not in visited:
                for elem in graph[curr]:
                    if elem not in visited:
                        q.append(elem)
                visited.add(curr)

            size -= 1
            if size == 0 and len(q) != 0:
                size = len(q)
                h += 1
        
        return h
        