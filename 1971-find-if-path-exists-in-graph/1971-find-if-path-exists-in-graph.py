'''
37
problem:
    given a list of edges, source and destination, return whether there is a valid path from source to destination
input:
    list of edges
work:
    find whether two nodes are connected
output:
    boolea, are the edges connected?

ideas:
    build a graph then travers from source to destination
    t = O(V+E) s = O(V+E)
    
    quick union find with path compression
    t = O(E) amortized s = O(V)
'''
class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        #find the number nodes
        num_v = 0
        for edge in edges:# bug, looked through edges instead of maximum label
            for v in edge:
                num_v = max(num_v, v)
        num_v += 1
        uf = UnionFind(num_v)
        #apply union to all edges
        for v1,v2 in edges:
            uf.union(v1,v2)
        return uf.find(source) == uf.find(destination)
            
        
        #determine whether source and destination have the same find
class UnionFind:
    def __init__(self, size):
        self.v = [-1] * size
    
    def union(self,v1,v2):
        g1 = self.find(v1)
        g2 = self.find(v2)
        if g1 == g2:
            return
        #take the size of the smaller one to point to the bigger one
        size1 = self.v[g1]
        size2 = self.v[g2]
        if abs(size1) <= abs(size2):
            #merge to size2
            self.v[g2] += self.v[g1]
            self.v[g1] = g2
        else:
            self.v[g1] += self.v[g2]
            self.v[g2] = g1
    def find(self, v):
        
        if self.v[v] < 0:
            return v
        self.v[v] = self.find(self.v[v])
        return self.v[v]