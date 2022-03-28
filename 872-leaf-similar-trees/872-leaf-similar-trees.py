# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
19
problem:
    given the roots of 2 binary trees( root1, root2) return if they have the same leaf value sequence
input:
    root1
    root2 head of binary tree
work:
    determine if they have the same leaf value sequence
output:
    boolean: have the same leaf sequence?
examples:
    given in prompt
ideas:
    perform a dfs on both tree to find all leaves then compare
    s(O(root1+root2)) t(O(root1+root2))
    
    opt:
        O(min(root1,root2) + max(height)) t(O(root1+root2))
'''
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        #nodes between 1 and x so no need to null check
        def findLeaves(root):
            sol = []
            curr = root
            stack = []
            while curr or stack:
                while curr:
                    stack.append(curr)
                    curr = curr.left #bug, traversed as list not as tree
                curr = stack.pop()
                if not (curr.left or curr.right):
                    sol.append(curr.val)
                curr = curr.right
            return sol
        
        leaves1 = findLeaves(root1)
        leaves2 = findLeaves(root2)
        if len(leaves1) != len(leaves2):
            return False
        trav = 0
        while trav < len(leaves1):
            if leaves1[trav] != leaves2[trav]:
                return False
            trav+=1
        return True
                    
            
        