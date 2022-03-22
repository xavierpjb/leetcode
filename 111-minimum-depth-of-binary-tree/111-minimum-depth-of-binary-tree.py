# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
17 - 32
problem given the head of a binary tree, return its min depth (shortest path from root to leaf counting each node)

input:
    root: Treenode -> root of the binary tree ( can be None)
work:
    find the smallest depth
output:
    int: shortest depth

examples:
    see examples provided
tests:
no node

varying node depths
'''
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        #find min depth
        minDep = [float('inf')]
        def minDH(node, depth):
            if not node:
                return
            
            depth += 1
            if depth >= minDep[0]: #stop if we already have a better candidate
                return

            if not (node.left or node.right): #bug, did not properly identify a leaf node
                minDep[0] = depth
                return
            minDH(node.left, depth)
            minDH(node.right, depth)
            
        minDH(root,0)
        return minDep[0]
        
        
        