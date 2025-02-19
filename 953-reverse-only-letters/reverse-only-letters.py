class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        def isEnglishLetter(c):
            return (ord("a") <= ord(c) and ord(c) <= ord("z")) or (ord("A") <= ord(c) and ord(c) <= ord("Z"))

        l, r = 0, len(s) - 1

        ans = list(s)

        while l < r:
            while l < r and not isEnglishLetter(s[l]):
                l += 1
            while l < r and not isEnglishLetter(s[r]):
                r -= 1
            ans[l], ans[r] = ans[r], ans[l]
            l += 1
            r -= 1
        return "".join(ans)
            