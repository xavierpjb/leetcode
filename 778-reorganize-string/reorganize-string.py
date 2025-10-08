'''
problem
  input:
    s: string that may contain letters that are adjacent
  work:
    if possible generate a string which contains no adj string
  output
    s: string that has no adj same letters or empty

  examples
ideas:
  how to order string base on number of available chars
as long as

'''

class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = {}
        for c in s:
            if c not in counts:
                counts[c] = 0
            counts[c] += 1
        sortedCounts = sorted(counts.items(), key=lambda x: -x[1])

        firstElem = sortedCounts[0]
        c, count = firstElem
        limit = len(s)//2
        if len(s) % 2 != 0:
            limit += 1
        if count > limit:
            return ""
        ans = ["" for _ in range(len(s))]
        x = 0
        i = 0
        while x < len(s):
            c, count = sortedCounts[i]
            sortedCounts[i] = (c, count - 1)
            ans[x] = c
            if count - 1 == 0:
                i += 1
            x += 2
        x = 1
        while x < len(s):
            c, count = sortedCounts[i]
            sortedCounts[i] = (c, count - 1)
            ans[x] = c
            if count - 1 == 0:
                i += 1
            x += 2
        return "".join(ans)
            

        

    
        