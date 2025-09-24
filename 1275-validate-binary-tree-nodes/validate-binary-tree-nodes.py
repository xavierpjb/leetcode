'''
toplogical sort where all nodes have at most 1 in degree
'''
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # create a list of in degrees
        # if no nodes have an in degree of 0, return false
        # if more than one node has 0 in degree return false
        # if any node has an in degree of more than 1, return false
        indegree = [0] * n

        for curr in range(n):
            left = leftChild[curr]
            if left != -1:
                indegree[left] += 1
            right = rightChild[curr]
            if right != -1:
                indegree[right] += 1

        num0In = 0
        start = None
        for i, ind in enumerate(indegree):
            if ind == 0:
                num0In += 1
                start = i

        if num0In != 1:
            return False
        
        for ind in indegree:
            if ind > 1:
                return False
        
        q = [start]
        numElem = 0
        while q:
            curr = q.pop()
            numElem += 1
            left = leftChild[curr]
            if left != -1:
                indegree[left] -= 1
                if indegree[left] == 0:
                    q.append(left)
            right = rightChild[curr]
            if right != -1:
                indegree[right] -= 1
                if indegree[right] == 0:
                    q.append(right)

        return numElem == n

        