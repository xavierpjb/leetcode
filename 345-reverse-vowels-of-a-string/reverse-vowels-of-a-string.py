'''
problem:<

exapmles: <

scenarios:
lmnopqu
lmnupqo

input: s
work: reverse vowel
output: string reverse

ideas:

isVowel aeiouAEIOU

while l is not in vowel
while r is not in vowel
leod
loed

joint
aaaaaaaooooooo
oaaaaaaooooooa
oo..........aa

[a,a,a,a,a,o,o,o]
""
'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s) - 1
        vowels = {"a", "e", "i", "o", "u", "A","E", "I", "O", "U"}
        s = list(s)
        while l < r:
            while l < r and s[l] not in vowels:
                l += 1
            
            while l < r and s[r] not in vowels:
                r -= 1

            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l += 1
            r -= 1
            
        return "".join(s)
        '''
        [l,l]
        r
             l
        '''





        