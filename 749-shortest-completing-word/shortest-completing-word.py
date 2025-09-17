'''
Problem:
  input: 
    licensePlate: string
    words: string[]
  work:
    find shortest completing word
    completing word = word that contains all characters in license palte (igore nums)
  output:
    shortesCompeteWord : string

examples:
  
ideas:
 given that we don't care about order, turn chars into a map then go through all strings and transform them as well
'''
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        lPCharMap = self.charMap(licensePlate)
        ans = None
        for word in words:
            if not ans:
                wCharMap = self.charMap(word)
                if self.isCompletingWord(lPCharMap, wCharMap):
                    ans = word
            else:
                if len(ans) <= len(word):
                    continue
                wCharMap = self.charMap(word)
                if self.isCompletingWord(lPCharMap, wCharMap):
                    ans = word
        return ans
                

    def charMap(self, s):
        m = {}
        for c in s:
            if c.isalpha():
                c = c.lower()
                if c not in m:
                    m[c] = 0
                m[c] += 1
        return m
    
    def isCompletingWord(self, lPCharMap, wCharMap):
        for c, count in lPCharMap.items():
            if c not in wCharMap:
                return False
            if wCharMap[c] < count:
                return False
        return True


        