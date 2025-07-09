'''
scenarios:

0: 1
1: <>

if you reach the end, return curr path
if no more nodes to visit, return
'''

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        graphC = Grapher(graph)
        return graphC.paths

class Grapher:
    def __init__(self, graph):
        self.graph = graph
        self.path = [0]
        self.paths = []
        self.fillPaths(self.graph[0])
    
    def fillPaths(self, nextNodes):
        for node in nextNodes:
            self.path.append(node)
            if node == len(self.graph) - 1:
                self.paths.append(self.path[:])
            else:
                self.fillPaths(self.graph[node])
            self.path.pop()


        
        