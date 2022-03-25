# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
problem:
    given the root of a binary tree, return the level order trav in reverse
    
input:
    root: TreeNode, head of the binary tree
work:
    level order traversal from bottom to top
output:
    list int[]: level order traversal from top to bottom

examples:
    given in prompt

idea:
    perform a regular bfs then reverse the output
    t = O(n) s = O(n)

test:

    no nodes
    
    varying height of trees
'''
from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = [[]]
        q = deque([root])
        size = 1
        while q:
            curr = q.popleft()
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
            ans[-1].append(curr.val)
            
            size -= 1
            if not size:
                size = len(q)
                if size:
                    ans.append([])
        ans.reverse()
        return ans
    '''
    
    '''
                
                
            
        
        
        
        
        