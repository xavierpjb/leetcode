# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

'''
Problem: <
examples:
list of only nums, check is int and
process list and maintain an index

[1,2,3]

return [1,2,3]

[1,[2,3,[4,5],6]]

recursively go through
tc = n sc = n

q?
append everything in a deque
while processing if in return num
if list append to front of qu

[1,[2,3,[4,5]6]
[[2,3,[4,5]6]]
[2,3,[4,5]6] n^2?

travers list and append 

recursion

if num append to list and return
if list enter


'''
from collections import deque
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.ans = deque()
        self.genAns(nestedList)
        
    def genAns(self, nestedList):
        for nestedElem in nestedList:
            if nestedElem.isInteger():
                self.ans.append(nestedElem.getInteger())
            else:
                self.genAns(nestedElem.getList())

    
    def next(self) -> int:
        return self.ans.popleft()
        
    
    def hasNext(self) -> bool:
        return len(self.ans) != 0
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())