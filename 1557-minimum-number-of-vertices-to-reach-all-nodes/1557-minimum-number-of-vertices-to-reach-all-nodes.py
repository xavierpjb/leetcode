'''
42
problem:
    given a list of edges and the numbers of vertices, return the smallest set of vertics all nodes are reachable
input:
    n: number of vertices
    edges: int[][] connections
work:
    find the smallest graph that all trees are reachable
output:
    find smallest set of vertices which all nodes are reachable
output:
    int[]: list of vertices
    
examples:
    given in prompt
ideas:
    bf:
    find all vertices that have an in degree of 0
    t = O(edges) computing in degrees s = O(N) for storing in degs
'''
from collections import defaultdict
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # create a map of indegrees
        inDegs = defaultdict(int)
        for f, t in edges:
            inDegs[t] += 1
        #find all vertices with an in degree of 0
        sol = []
        for i in range(n):
            if inDegs[i] == 0:
                sol.append(i)
                
        return sol
                
        