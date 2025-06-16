"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
'''
Problem:
populate right pointer of a node
examples: <
scenarios:
[] [1] [1,2], [1,2,3]
input root
work populate root.right
output: root

ideas:

use a qeue for level order trav, go through each level and set right to next elem

s = o(n)
t = o(n)
'''
from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        q = deque([root])
        lvlSize = 1
        while q:
            elem = q.popleft()
            lvlSize -= 1
            if elem.left:
                q.append(elem.left)
            if elem.right:
                q.append(elem.right)
            if lvlSize == 0 and q:
                for i in range(len(q) - 1):
                    elem = q.popleft()
                    elem.next = q[0]
                    q.append(elem)
                q.append(q.popleft())
                lvlSize = len(q)    

        return root

        