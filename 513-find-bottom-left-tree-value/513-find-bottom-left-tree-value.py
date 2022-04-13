# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
problem:
    given the root of a binary tree, return the leftmost val in the last row
input:
    root: TreeNode, head of binary treee
work:
    find the leftmost node of the last row of the tree
output:
    int: value of said node
examples:
    given in prompt

ideas:
    perform a dfs and only update when we reach a new depth
    
    perform bfs and get the first value of every new depth
'''
from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        size = 1
        lm = root.val
        while q:
            curr = q.popleft()
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
            size -= 1
            if q and size == 0:
                lm = q[0].val # bug, did not take the val
                size = len(q)
        return lm
    '''
    
    '''
        
        