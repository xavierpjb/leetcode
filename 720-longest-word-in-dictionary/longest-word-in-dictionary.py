'''
put in trie then traverse and  stop once word can be completed


w o 
  * *


create a trie

Traver trie and append to sol iff word is terminal and has next, other


ideas:
sort by lenght then lookup maps for words of length smaller


'''

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.addWord(word)
        return trie.findLongestWord()

class Trie:
    def __init__(self):
        self.root = {"*":{}}

    def addWord(self, word):
        currMap = self.root
        for c in word:
            if c not in currMap:
                currMap[c] = {}
            currMap = currMap[c]
        currMap["*"] = {}

    def findLongestWord(self):
        #recursively lookup words that are both
        currSol = [""]
        self.rec(self.root, [], currSol)
        return currSol[0]

    def rec(self, cMap, currWord, currSol):
        for oc, oMap in cMap.items():
            if oc != "*" and "*" in oMap:
                currWord.append(oc) #wrong map ref
                self.rec(oMap, currWord, currSol)
                if len(currWord) > len(currSol[0]):
                    currSol[0] = "".join(currWord)
                elif len(currWord) == len(currSol[0]):
                    currSol[0] = min(currSol[0], "".join(currWord))
                currWord.pop()


        