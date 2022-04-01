# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
22
problem:
    given the root of a binary tree return the number of nodes in the tree
    a complete binary tree is where all nodes except last are filled, last are filled ltr
    at the last level h it can have between 1 and 2h nodes
    
input:
    root: treenode, root of the complete binary tree
work:
    find the number of nodes
output:
    int: number of nodes in the tree
examples:
    given in the prompt
ideas:
    bf, count every node
    t = O(n), s = O(h) where h is the height of the tree
    
    optimized
    everything up to the height of the tree is complete
    at height h you have between 2^0 + 2^1 + ... +2^(h-1) + [1...2^h]
    how to get the value of 1..2^h ( go to the last level and count the children)
    how to get the rightmost node?
    do a binary search for leafs?
    how to get a leaf between 1 and 2^h in logn time?
    look for a branch and divide the search space in half each time
'''
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not (root.left or root.right):
            return 1
        #find height
        height = 0
        trav = root
        while trav.left:
            height += 1
            trav = trav.left
        last_full = height - 1
        nodes_to_lf = 2**(last_full+1) - 1
        
        l = 0
        r = 2**height - 1
        def condition(target):
            lower = 0
            upper = 2**height - 1
            tail = root
            for x in range(height+1):
                if not tail:
                    return False
                mid = (lower+upper)//2
                if lower <= target <= mid:
                    tail = tail.left
                    #bug, did not update upper and lower bounds
                    upper = mid
                else:
                    tail = tail.right
                    lower = mid+1
            return True
        while l < r:
            mid = ceil((l+r)/2)#Buuuuuuug, integer division when using ceiling
            if condition(mid):
                l = mid
            else:
                r = mid - 1
        return nodes_to_lf + l + 1
        #find the height of the tree and calculate the number of nodes up to height
        
        
        #guess what the last node is and search