# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
30
problem:
    given root of bst, rearrange in order so we get a linked list ( no node has a left child)

input:
    head: Treenode, head of the bst
work:
    transform into a ll with root as the leftmost node
output:
    Treenode, head of new list
examples:
    given in prompt

ideas:
    bf:
    store inorder traversal into a list t(n) s(n)
    
    improved space worse time:
    find successor of each node
    would yield nlogn time (each node would need to lookup successor) t(nlogn) s(h) where h = height of tree
    
    improved time and space: #implementing this
    keep a global tail and update as we traverse t(n) s(h)
    
    linear time const space:
    traverse using morris traversal
    
    
'''
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        tail = TreeNode()
        def helper(node,tail):
            if not node:
                return
            helper(node.left,tail)
            node.left = None
            tail[0].right = node
            tail[0] = tail[0].right
            helper(node.right,tail)
        helper(root,[tail])
        return tail.right
            
            
            
        