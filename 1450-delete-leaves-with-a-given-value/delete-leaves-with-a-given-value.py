'''
start with dummy node
post order trav, if 
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        dummy = TreeNode(0,root, None)
        self.dfs(dummy, target)
        return dummy.left

    def dfs(self, node, target):
        if not node:
            return True
        l, r = self.dfs(node.left, target), self.dfs(node.right, target)

        if l:
            node.left = None
        if r:
            node.right = None
        
        if not (node.left or node.right):
            return node.val == target
        return False
        