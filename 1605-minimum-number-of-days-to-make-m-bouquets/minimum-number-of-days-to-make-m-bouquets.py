'''
invalid bouquets

more boquets then possible
need at least k*m elems


'''
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < k*m:
            return -1

        def isValid(day):
            #can you form m arrays of size k
            x = 0
            numBouquets = 0
            while x + k - 1 < len(bloomDay):
                if bloomDay[x] > day:
                    x += 1
                    continue
                if canFormBouquet(x, day):
                    numBouquets += 1
                    if numBouquets == m:
                        return True
                    x += k
                else:
                    while bloomDay[x] <= day:
                        x += 1

            return False

        def canFormBouquet(startingPoint, day):
            for x in range(startingPoint, startingPoint + k):
                if bloomDay[x] > day:
                    return False
            return True
        l, r = 1, max(bloomDay)
        while l < r:
            mid = (l+r) // 2
            if isValid(mid):
                r = mid
            else:
                l = mid + 1

        return l