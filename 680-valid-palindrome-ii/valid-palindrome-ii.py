class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isValidPalindrome(allowError, l, r):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                elif allowError:
                    return isValidPalindrome(False, l+1, r) or isValidPalindrome(False, l, r-1)
                else:
                    return False

            return True
        return isValidPalindrome(True, 0, len(s) - 1)