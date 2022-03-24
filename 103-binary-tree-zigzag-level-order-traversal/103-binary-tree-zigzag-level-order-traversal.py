# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
problem:
    given the root of a binary tree, return the zigzag level order trav(ltr then rtl)

input:
    root: treenode, head of the binary tree
work:
    return a list of level order traversal by zig zag
output:
    list node values in zig zag

examples:
    given in prompt

ideas:
    do a bfs but instead of popping from q, add to list and figure out wether to reverse list
'''
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        sol = []
        if not root:
            return []
        sol.append([root])
        shouldRev = False
        
        while sol[-1]:
            sol.append([])
            for x in range(len(sol[-2])):
                node = sol[-2][x]
                if node.left:
                    sol[-1].append(node.left) #bug, should be putting values not the node itself
                if node.right:
                    sol[-1].append(node.right)
                sol[-2][x] = node.val
                
            if shouldRev:
                sol[-2].reverse()
            shouldRev = ~shouldRev
        sol.pop()
        return sol
    '''
    shouldReve = True
    [[3][20,9][15,7]]
    '''
        