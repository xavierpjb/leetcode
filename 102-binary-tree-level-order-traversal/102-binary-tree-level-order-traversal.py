# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
given the root of a binary tree return the level order traversal

input:
    root
work:
    give the inorder traversal
output:
    list node values by level

examples:
    given in prompt

idea:
    do a bfs on tree and appends level to solution
    t = n s = n
'''
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        size = 1
        lvl = 1
        l_order = [[root.val],[]]
        while q:
            curr = q.popleft()
            if curr.left:
                q.append(curr.left)
                l_order[lvl].append(curr.left.val)
                
            if curr.right:
                q.append(curr.right)
                l_order[lvl].append(curr.right.val)
            
            size -= 1
            if size == 0:
                size = len(q)
                lvl += 1
                if q:
                    l_order.append([])
        l_order.pop()
        return l_order
    '''
    [[3],[9,20],[15,7][]]
    q = [15,7]
    curr = 20
    '''
                
            
        