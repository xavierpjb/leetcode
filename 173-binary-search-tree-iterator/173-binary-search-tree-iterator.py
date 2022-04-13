# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
44
problem
    given the root of a bst, make an iterator class that generates the inorder traversal with next, 
    and keeps track of has next
input:
    root: treenode given in the constructor
work:
    provide the next node
    provide if there is a next node
output:
    the next node
    a boolean denoting if there is a next node
examples:
    given in prompt
ideas:
    perform iterative traversal of binary tree while keeping track of the stack of nodes to travers
    
'''
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.curr = None
        if not root:
            return
        trav = root
        while trav and trav.left:
            self.stack.append(trav)
            trav = trav.left
        self.curr = trav #bug, processessed stack elements twice
        
        

    def next(self) -> int:
        ret = self.curr
        if self.curr.right:
            trav = self.curr.right
            while trav and trav.left:
                self.stack.append(trav)
                trav = trav.left
            self.curr = trav#bug, processessed stack elements twice
        elif self.stack:
            self.curr = self.stack.pop()
        else:
            self.curr = None
        
        return ret.val
        

    def hasNext(self) -> bool:
        return self.curr != None
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()