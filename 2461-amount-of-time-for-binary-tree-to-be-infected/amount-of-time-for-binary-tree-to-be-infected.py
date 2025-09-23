'''
problem:
  input:
    root: Treenode, tree containing an infected node
  work: find the number of bfs hops from start index
  output:
    minutesFullInfection: int
  examples:
    
ideas:
 perform bfs on tree for time
 create graph then traverse


'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = {}
        graph[root.val] = []
        if root.left:
            self.buildGraph(root.left, root.val, graph)
        if root.right:
            self.buildGraph(root.right, root.val, graph)

        #starting at start, perform a bfs and count number of hops
        q = deque([start])
        visited = set()
        size = 1
        hops = 0
        while q:
            curr = q.popleft()
            visited.add(curr)
            for nei in graph[curr]:
                if nei not in visited:
                    q.append(nei)
            size -= 1
            if size == 0:
                hops += 1
                size = len(q)            
        
        return hops - 1


    def buildGraph(self, node, parentId, graph):
        if not node:
            return
        graph[parentId].append(node.val)
        graph[node.val] = []
        graph[node.val].append(parentId)
        self.buildGraph(node.left, node.val, graph)
        self.buildGraph(node.right, node.val, graph)

