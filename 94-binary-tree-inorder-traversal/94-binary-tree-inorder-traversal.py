# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        sol = []
        if not root:
            return sol
        
        stack = []
        curr = root
        
        while curr or stack:
            if curr and curr.left:
                while curr.left:
                    stack.append(curr)
                    curr = curr.left
            else:
                if not curr:
                    curr = stack.pop()
                sol.append(curr.val)
                curr = curr.right
        
            
        return sol
        