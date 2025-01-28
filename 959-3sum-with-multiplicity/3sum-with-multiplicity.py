
'''
5,3,1

2 sum of unordered in linear time
duplicate numbers with varying indexes
3,5 vs 5,3
0 1    0 1
if they're in different indexes, does it matter?
1,2,3,4 vs 3,4,2,1 target = 5
0 1 2 3    0 1 2 3
(0,3) (1,2)    (0,2) (1,3)


2,2,2,2,2 4
0,1,2,3,4
01 02 03 04
12 13 14
23 24
34 = (n)*(n-1)/2 duplicates
1,2,2 = 
1*2 = n1* n2 for non duplicates

add a 3rd number
distinct
 n2* n3
3,3,3,3,
0,1,2,3
012 013 023
123
'''

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        sols = 0
        i = 0
        while i < len(arr) - 2:
            rem = target - arr[i]
            l, r = i + 1, len(arr) - 1
            while l < r:
                lr = arr[l] + arr[r]
                if lr == rem:
                    if arr[l] == arr[r]:
                        sols += (r - l + 1) * (r - l) // 2
                        l = r
                    else:
                        numL = 1
                        l += 1
                        while arr[l-1] == arr[l]:
                            numL += 1
                            l += 1
                        numR = 1
                        r -= 1
                        while arr[r] == arr[r+1]:
                            numR +=1
                            r -=1
                        sols += numR * numL
                elif lr > rem:
                    r -= 1
                else:
                    l += 1

            i += 1

        return sols % (10**9 + 7)
        