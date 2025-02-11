'''
Problem: <

examples: <

scenarios

123 > 132 > 213 > 231 > 312 > 321

1234 > 1243 > 1342 > 15

12345 > 12354 > 12453
                12435 > 12453 > 12543
                                12534
                                598765432

same as next possible sequence

if numbers are completely ascending return -1
if number is > 2^31 - 1 return -1

find first non ascending number, then swap with first number > from the right and sort end of number

'''
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if n < 10:
            return -1

        def findSwap():
            num = n
            power = 1
            digitFromRight = num % 10
            num //= 10
            while num != 0:
                nextDigit = num % 10
                if nextDigit >= digitFromRight:
                    digitFromRight = nextDigit
                    num //= 10
                    power += 1
                else:
                    return power      
            return -1
        
        swapPoint = findSwap()
        if swapPoint < 1:
            return -1
        #find first number > swap point
        def findRep(power):
            num = n
            digit = (num // 10**power) % 10
            oPower = 0
            oDig = num % 10
            num //= 10
            while True:
                if oDig > digit:
                    return oPower
                oPower += 1
                oDig = num % 10
                num //= 10
        
        rep = findRep(swapPoint)

        def swapPows(num, power1, power2):
            dig1 = (num // 10**power1) % 10
            dig2 = (num // 10**power2) % 10

            num -= dig1 * 10**power1
            num += dig2 * 10**power1
            num -= dig2 * 10**power2
            num += dig1 * 10**power2
            return num
        n = swapPows(n, swapPoint, rep)

        def revUpTo(num, point):
            l = 0
            r = point - 1
            while r > l:
                num = swapPows(num, l, r)
                l += 1
                r -= 1
            return num

        num = revUpTo(n,swapPoint)

        if num <= 2**31-1:
            return num
        return -1

        
