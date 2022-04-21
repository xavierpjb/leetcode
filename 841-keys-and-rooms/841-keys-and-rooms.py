'''
11
problem:
    given a set of rooms and a set of keys, return whether you can visit all rooms
input:
    rooms: int[][] rooms with keys
work:
    traverse the rooms to find if all rooms can be opened
output:
    bool: whether all rooms can be traversed
examples:
    given in prompt
ideas:
    do a traversal of each key found, while tracking visited rooms
    t = O(n), s = O(n)
    
'''
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        #dfs traversal of non visited         
        def dfs(source):
            if len(visited) == len(rooms):
                return True
            for key in rooms[source]:
                if key not in visited:
                    visited.add(key)
                    if dfs(key):
                        return True
            return False
        return dfs(0)
                    
                    
        
        