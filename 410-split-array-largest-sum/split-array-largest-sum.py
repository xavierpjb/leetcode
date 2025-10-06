'''
in linear time we can tell whether a k is valid
n log sum off all elements

such that all sums less than target sum
'''
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        ans = 0
        def isValidWithMaxSum(maxSum):
            # create arrays of at most size elements and
            numSubArr = 1
            currSum = 0
            for num in nums:
                if num > maxSum:
                    return False
                if currSum + num > maxSum:
                    numSubArr += 1
                    if numSubArr > k:
                        return False
                    currSum = num
                else:
                    currSum += num
                     
            return True

        l, r = max(nums), sum(nums)
        while l < r:
            mid = (l+r) // 2
            if isValidWithMaxSum(mid):
                r = mid
            else:
                l = mid + 1
        return l



        