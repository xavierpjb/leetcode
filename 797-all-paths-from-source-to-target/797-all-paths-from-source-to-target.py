'''
30
problem:
    given a dag of n nodes find all possible paths from 0 to n-1 in any order
input:
    graph: int[][] where graph[i] = all nodes accessible from i
work:
    find all paths from 0 to n-1
output:
    all paths from 0 to n-1
examples:
    given in prompt
idea:
    perform a dfs from  0 to target, since it's a dag, we don't need to keep track of visited 
    (since this would cause inf loops)
    t = O(V+E) s = O(number of possible paths)
    
    
'''
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        sol = []
        def dfs(target, slate):
            if slate[-1] == target:
                sol.append(slate.copy())
                return
            for nextPath in graph[slate[-1]]:
                slate.append(nextPath)
                dfs(target,slate)
                slate.pop()
        
        dfs(len(graph) - 1,[0])
        return sol
            
        