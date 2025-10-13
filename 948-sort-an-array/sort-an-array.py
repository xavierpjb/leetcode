class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        h = Heap()
        for num in nums:
            h.push(num)

        ans = []
        while h.arr:
            ans.append(h.pop())
        return ans
class Heap:
    def __init__(self):
        self.arr = []
    
    def push(self, x):
        # add to the end, then swim to top
        self.arr.append(x)
        self.swim(len(self.arr) - 1)

    def pop(self):
        self.arr[0], self.arr[len(self.arr)-1] = self.arr[len(self.arr)-1], self.arr[0]
        ans = self.arr.pop()
        self.sink(0)
        return ans
    
    def sink(self, i):
        #pick the smaller of the 2 children, put it on top, repeat with the replaced node
        iSmall = i
        iL = (2*i) + 1
        if iL < len(self.arr) and self.arr[iL] < self.arr[iSmall]:
            iSmall = iL

        iR = (2*i) + 2
        if iR < len(self.arr) and self.arr[iR] < self.arr[iSmall]:
            iSmall = iR
        if iSmall != i:
            self.arr[iSmall], self.arr[i] = self.arr[i], self.arr[iSmall]
            self.sink(iSmall)

    def swim(self, i):
        if i == 0:
            return
        iParent = (i-1) // 2

        if self.arr[i] < self.arr[iParent]:
            self.arr[i], self.arr[iParent] = self.arr[iParent], self.arr[i]
            self.swim(iParent)
        

        