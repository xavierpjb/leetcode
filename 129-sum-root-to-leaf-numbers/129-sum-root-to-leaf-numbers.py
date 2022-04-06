# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
problem:
    given the root of a binary tree, add the sum of the root to leaf numbers
input:
    root of a tree
work:
    add the sum of all root to leaf numbers
output:
    int: sum of all the numbers
examples:
    given in prompt
idea:
    have a running sum of each branch path, add to global sum when leaf is reached
    s = O(h), t = O(n)
test:
    one node
    multiple nodes
'''
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def sumNumHelper(node, sum_so_far):
            if not node:
                return 0
            
            sum_so_far *= 10
            sum_so_far += node.val
            if not (node.left or node.right):
                return sum_so_far
            return sumNumHelper(node.left, sum_so_far) + sumNumHelper(node.right, sum_so_far)
        return sumNumHelper(root, 0)
    '''
    12 13
    
    '''
            
            
        