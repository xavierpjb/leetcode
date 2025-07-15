'''
problem: given a list of edges, return the number of complete components
 example<
 scenarios 0: {}  1: {} return 2
          0: {1}  1: {0} return 1
          0: {1,2} 1: {0} 2:{0} return 0
input
  n: number of edges
  edges: connections between edges
work
  find number of completely connected components
output:
  int number of completely connected  

ideas:

convert to graph O(e)


---INVALID
if any node does not have the same number of connections as its
0:1,2   1:0,2,3   2:0,1   3:1,2
0 - 1 - 3
| /   /
2 ---

0 - 1 - 2 - 3
 \---------/


--- VALID ----
(?)find size ofconnected components: O(e)

or get component size and check every node has size-1 connections

'''
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {x:[] for x in range(n)}

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        sizer = ComponentSizer(graph)
        count = 0
        for vertex, nbors in graph.items():
            if vertex in sizer.visited:
                continue
            cSize = sizer.getSizeForComponentAt(vertex)
            if len(nbors) != cSize - 1:
                continue
            isComplete = True   
            for nbor in nbors:
                if len(graph[nbor]) != cSize - 1:
                    isComplete = False
                    break
            count += 1 if isComplete else 0      
        return count

class ComponentSizer:
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()
    
    def getSizeForComponentAt(self, vertex):
        if vertex in self.visited:
            return 0
        self.visited.add(vertex)
        size = 1
        for nbor in self.graph[vertex]:
            size += self.getSizeForComponentAt(nbor)
        return size





        