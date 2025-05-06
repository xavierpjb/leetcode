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
        self.q1 = deque()
        self.q2 = deque()
        

    def push(self, x: int) -> None:
        self.q1.append(x)
        

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        ans = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return ans
        

    def top(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        ans = self.q1.popleft()
        self.q2.append(ans)
        self.q1, self.q2 = self.q2, self.q1
        return ans
        

    def empty(self) -> bool:
        return len(self.q1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()