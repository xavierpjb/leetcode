'''
find the depth of the tree then return the path to it

if coming from right, return depth zag at left
if coming form left return zag at right
for self, pick max betwen zag left and right,

  return zag left + 1 if right of parent
  return zag right + 1 if left of parent
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        dfs = Dfs()
        return dfs.trav(root, None) - 1

class Dfs:
    def __init__(self):
        self.ans = 0


    def trav(self, node, parent):
        if not node:
            return 0
        
        l = self.trav(node.left, node)
        r = self.trav(node.right, node)

        ansAtCurr = max(l,r) + 1
        if ansAtCurr > self.ans:
            self.ans = ansAtCurr

        if not parent:
            return self.ans
        if node == parent.left:
            return 1 + r
        else:
            return 1 + l
        

        