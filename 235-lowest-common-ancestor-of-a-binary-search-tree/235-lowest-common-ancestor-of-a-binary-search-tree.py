# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
problem:
    given the root of a bst, find the lowest common ancestors of two nodes. Both nodes will exist
    node can also be an ancestor

input:
    treeNode: root of the binary tree
work:
    find the lca
ouptput:
    treeNode: lca

examples:
    given in prompt
ideas:
  find one of the two elements and  return the node wherea split needs to happen ( find on of the elements or find a spliting element)
  t = O(h), s = o1
'''

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        trav = root
        while True:
            if min(p.val,q.val) <= trav.val <= max(p.val,q.val):
                return trav
            if trav.val > p.val:
                trav = trav.left
            else:
                trav = trav.right
            