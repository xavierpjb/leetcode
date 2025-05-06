'''
input: n/a
work: provide methods for stack
output: method for stack

ideas:

q is fifo

1,2,3

push everything but last element to q
push(o1)
pop(on)
top(on)
empty(o1)


'''
from collections import deque
class MyStack:

    def __init__(self):
        self.q = deque()
        

    def push(self, x: int) -> None:
        self.q.append(x)
        

    def pop(self) -> int:
        for i in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

        return self.q.popleft()
        

    def top(self) -> int:
        for i in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
        
        ans = self.q.popleft()
        self.q.append(ans)
        return ans
        

    def empty(self) -> bool:
        return len(self.q) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()