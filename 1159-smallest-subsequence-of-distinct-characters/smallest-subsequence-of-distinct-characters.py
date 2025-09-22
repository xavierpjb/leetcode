'''
problem:
  input:
    s: string
  work:
    find lexicographically smalles subsequence containg all distict 
  output:
    s: answer from work

examples

bacde

have to have at least one instance of each char

accccddddbccccaaaaaabbbd

bf solution
find all unique chars
create permumations from smallest to larget
find if subsequence exists
tc = n*n!

find all unique chars
3121

how to determine first char? second char? 3rd char?
last instance. if there are more instances of a smaller char left then no need to include
have a list, determine if you can remove or add the char
while process string, if you find a smaller char and there's more chars left, remove, otherwise continue

first instance 


'''
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        count = {}
        for c in s:
            if c not in count:
                count[c] = 0
            count[c] += 1
        
        ans = [s[0]]
        count[s[0]] -= 1
        included = set(s[0])
        x = 1
        while x < len(s):
            curr = s[x]
            count[curr] -= 1
            while ans and curr < ans[-1] and curr not in included and count[ans[-1]] != 0:
                included.remove(ans.pop())
            
            if curr not in included:
                ans.append(curr)
                included.add(curr)
            x += 1


        return "".join(ans)


        
        