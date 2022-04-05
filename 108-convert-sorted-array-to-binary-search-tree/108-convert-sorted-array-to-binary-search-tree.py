# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # find the middle of the list, set it as the treenode and recurse left and right
        if not nums:
            return None
        def genBST(nums, l, r):
            if l > r:
                return None
            if l == r:
                return TreeNode(nums[l])
            mid = (l + r) // 2
            elem = TreeNode(nums[mid])
            elem.left = genBST(nums, l, mid-1)
            elem.right = genBST(nums, mid+1, r)
            return elem
        '''
        -10,-3,0,5,9
        l = 0, r = 4
        m = 2
        
        '''
            
            
        root = genBST(nums, 0, len(nums) - 1)
        return root
        
        