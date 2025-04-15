'''
problem:
examples
scenariois
input: list of temps
work: determine days till warmer
output: array of days

ideas
monotic stack
start out with 0 as answer
go through stack, and when remove
i - iStackElem
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = temperatures
        ans = [0] * len(temps)

        stack = []
        for i, val in enumerate(temps):
            while stack and temps[stack[-1]] < val:
                iStack = stack.pop()
                ans[iStack] = i - iStack
            stack.append(i)

        return ans
        