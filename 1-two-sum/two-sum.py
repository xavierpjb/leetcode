'''
Gave wrong time complexities for the problems
Could not say which sorting algorithms

Did not find optimal solution
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #some number + some other number need to add to target
        numToTarget = {}
        for i, num in enumerate(nums):
            if num in numToTarget:
                numToTarget[num].i.append(i)
            else:
                valNeeded = target - num
                ki = KeyIndex(valNeeded)
                ki.i.append(i)
                numToTarget[num] = ki
        
        for num, ki in numToTarget.items():
            valNeeded = ki.valNeeded
            if valNeeded in numToTarget:
                if valNeeded != num:
                    return (ki.i[0], numToTarget[valNeeded].i[0])
                if valNeeded == num and len(ki.i) > 1:
                    return (ki.i[0], ki.i[1])
                
class KeyIndex:
    def __init__(self, valNeeded):
        self.valNeeded = valNeeded
        self.i = []



        


        