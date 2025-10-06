'''
linear time minimum days to ship

'''
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def findNumDays(shipSize):
            numDays = 0
            spaceLeft = shipSize
            for weight in weights:
                if spaceLeft >= weight:
                    spaceLeft -= weight
                else:
                    numDays += 1
                    spaceLeft = shipSize - weight
            return numDays + 1
        #can't go beneath this
        l, r = max(weights), sum(weights)

        while l < r:
            mid = (l + r) // 2
            if findNumDays(mid) <= days:
                r = mid
            else:
                l = mid + 1
        return l

        

        