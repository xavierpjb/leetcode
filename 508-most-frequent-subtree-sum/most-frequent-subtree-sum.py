# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
generate all subtree sum then return the most frequently recuring one
'''
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        subSums = {}
        self.getSubSums(root, subSums)

        return self.getMostFrequent(subSums)
    
    def getSubSums(self, node, subSums):
        if not node:
            return 0
        l = self.getSubSums(node.left, subSums)
        r = self.getSubSums(node.right, subSums)
        total = node.val + l + r
        if total not in subSums:
            subSums[total] = 0
        subSums[total] += 1
        return total
    
    def getMostFrequent(self, subSums):
        mostFreq = 0
        ans = []
        for total, occ in subSums.items():
            if occ > mostFreq:
                mostFreq = occ
                ans = [total]
            elif occ == mostFreq:
                ans.append(total)
                
        return ans
        
        