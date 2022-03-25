"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
'''
31

problem:
    given the head of an n-ary tree, return the post order traversal

input:
    root: Node, root of the n-ary tree
output:
    int[], preorder traversal of the n-ary tree ( node values)
examples:
    given in prompt 
idea:
    bf:
    preorder recursive traversal
    
    iterative:
    add the children from right to left in stack
test:
    empty tree
    
    varying n tree
'''

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        ans = []
        stack = [root]
        
        while stack:
            curr = stack.pop()
            ans.append(curr.val)
            for node in reversed(curr.children):
                stack.append(node)
        return ans
        