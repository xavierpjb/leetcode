# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
started at 27
given the root of a bst, 2 nodes are swapped, recover the tree without changing its structure

input:
    root: root of bst
work:
    swap the valued of nodes which make the tree invalid
output:
    root: same root as passed in
    
examples:
    given in prompt
ideas:

Doing an inorder traversal will find where the tree is not in order
Doing a second search for placement will give you the spot to swap

            8
        5      10
       1 6    9   0
     11  2

To find offending node, find any element that is not within the wanted min max

How to find placement?
First number that breaks invariant when looking to place
look in subtree to find node that breaks invariant?

      7
    5      10
   3  6      11
  



Linear

Do an inorder traversal and store nodes in list
3,2,1

6,2,3,4,5,1
Find two numbers that swapped would result in ordered list
Increase then decrease, find number between the 2
if inorder traversal not monotonically increasing, prev node is the problem
swap with next 

1,5,7,9,10,11,
11,5,7,9,10,1

1,2,3,4,5
3,2,1,4,5

6,2,3,4,5,1,7,8

fix array in one swap
2 instances where we go hi to low
5,3,2,6
3,2
3,2,1
1,,4

3,1,2,4,5,3
8,5,6,7,8,1,9,10,20


swap min and max?

Pair of decrease

    
'''
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ans = []
        def inord(root):
            if not root:
                return
            inord(root.left)
            ans.append(root)
            inord(root.right)
        inord(root)
        pairs = []
        for i in range(1,len(ans)):
            if ans[i-1].val > ans[i].val:
                pairs.append((ans[i-1],ans[i]))
        a,b = pairs[0]
        if len(pairs) == 1:
            a.val, b.val = b.val, a.val
        else:
            c,d = pairs[1]
            a.val,d.val = d.val,a.val
        
        return root
        
            
                


        