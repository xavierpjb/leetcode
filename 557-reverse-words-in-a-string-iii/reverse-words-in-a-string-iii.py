class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = list(s)
        def rev(l,r):
            while l < r:
                words[l],words[r] = words[r], words[l]
                l+=1
                r-=1
        
        l = 0
        r = 1
        while l < len(words):
            while r < len(words) and words[r] != " ":
                r += 1
            rev(l,r-1)
            l = r + 1
            r += 1

        return "".join(words)
        