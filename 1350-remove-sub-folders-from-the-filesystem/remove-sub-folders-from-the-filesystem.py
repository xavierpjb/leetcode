'''
Problem
  input:
    folders: string[]
  work:
    determin sub folders
  output
    newFolders: string[] folders without subfolders

examples

scenarios
/a/b/c
/a
get rid of anything with a prefix

brute force
sort by len
remove any string which starts with smaller string
tc = numString * avgLen(strings) 

sort by len, create map of prefixes and look through

n*avlen(string)log(n*avlen string) + 

sort by len
process char as trie
how to know when end of string?

whenever we hit a /, check if end of character exists. if it does, stop processing
if we're able to store, add to answer




'''
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        sol = []
        trie = Trie()
        folder.sort(key=lambda x: len(x))

        for word in folder:
            if trie.processWord(word):
                sol.append(word)
        return sol

class Trie:
    def __init__(self):
        self.wordsTrie = {}
    
    def processWord(self, word):
        x = 1
        node = self.wordsTrie
        while x < len(word):
            curr = word[x]
            if curr == "/" and "*" in node:
                return False
            if curr not in node:
                node[curr] = {}
            node = node[curr]
            x += 1
        node["*"] = {}
        return True

        