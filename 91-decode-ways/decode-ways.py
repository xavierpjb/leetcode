'''
num ways at f(n) = 1? + f(n+1) + f(n+2)
num ways
num ways f(n) = num ways to decode group 1 + num ways to decode group 2

f(0) = 1 if not 0 else 0
f(1) = 


f(n) = number of ways to decode substring

bf, try every combination of 1 and 2 then check if all sub are valid up until end of string



solve for the last 2 then for the rest? what happens to cases wher you have a 0 leading? only consider prev is curr is valid




'''
class Solution:
    def numDecodings(self, s: str) -> int:
        #did not handle simple case
        c = 1 if int(s[-1]) > 0 else 0
        if len(s) == 1:
            return c

        b = 0
        if int(s[-2]) != 0:
            b = c
            if 9 < int(s[-2:]) < 27:
                b += 1

        for i in range(len(s) - 3, -1, -1):
            a = 0
            if int(s[i]) > 0:
                a += b
            if 9 < int(s[i:i+2]) < 27:
                a += c
            b, c = a, b

            # is current number valid and 
            #can you form a valid number with the one behind you
        

        return b


        
        
        


        
        

        