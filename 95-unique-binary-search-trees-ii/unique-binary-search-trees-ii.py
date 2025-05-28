# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
03
give n
return all structurally uniq bsts

input:
    int n: number of nodes (1,8)
output: list of head

examples
1
return 1

2
12
21
3

ideas:

    for every n, create all combs for lower and greater valuue

    [1,2,3,4]
    gen left, gen right
    for every number of list, set as root and call left and right on smaller and bigger
    [4,3,2]
    get sub range
    1
     2,3

    do a post order construction?

    for one element, 
    generate all possible combos to the left, generate all possible combos to the right
    create combinations at root

    for number in list
      reemove, gen left gen right
      for every number in left
        for every number in right
          use new range, append to list of roots

    return list of roots

'''
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def part(nums):
            val = nums[0]
            smaller, bigger = [], []
            for i in range(1, len(nums)):
                if nums[i] < val:
                    smaller.append(nums[i])
                else:
                    bigger.append(nums[i])
            return smaller,bigger

        def genTrees(nums):
            if len(nums) == 1:
                return [TreeNode(nums[0])]
            if len(nums) == 0:
                return []
            
            ans = []

            for i in range(len(nums)):
                nums[0],nums[i] = nums[i], nums[0]
                smaller, bigger = part(nums)
                leftSub = genTrees(smaller)
                rightSub = genTrees(bigger)
                rootVal = nums[0]
                if leftSub and rightSub:
                    for left in leftSub:
                        for right in rightSub:
                            root = TreeNode(rootVal, left, right)
                            ans.append(root)
                elif not leftSub:
                    for right in rightSub:
                        root = TreeNode(rootVal,None, right)
                        ans.append(root)
                else:
                    for left in leftSub:
                        root = TreeNode(rootVal,left, None)
                        ans.append(root)

                nums[0],nums[i] = nums[i], nums[0]
            return ans
        return genTrees([i for i in range(1,n+1)])
        


        
        