'''
work outside in
'''
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [set() for _ in range(n)]

        for edge in edges:
            x, y = edge[0], edge[1]
            graph[x].add(y)
            graph[y].add(x)

        leaves = []
        for node, nbor in enumerate(graph):
            if len(nbor) <= 1:
                leaves.append(node)

        while n > 2:
            newLeaves = []
            for leaf in leaves:
                for nbor in graph[leaf]:
                    graph[nbor].remove(leaf)
                    if len(graph[nbor]) == 1:
                        newLeaves.append(nbor)
                n -= 1
            leaves = newLeaves

        return leaves
        