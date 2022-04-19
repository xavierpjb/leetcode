'''
problem:
    given a list of trust relations, find a town judge if exists
input:
    n: int, number of people
    trust: int[][], edge representing trust relation
work:
    find if a judge exists
output:
    int: judge or -1
examples:
    given in prompt
    note: a judge trusts nobody but everybody trusts the judge, only one person satisfies 1 and 2
    rule 3 is useless
ideas:
    establish that rule 1 is possible, go through the list and ensure that only 1 person does not trust anyone
    once rule one possible, establish that all people trust the one non trusting person
    t = O(trust) s = O(n)
    
'''
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        #find out if only one person does not trust anyone
        nonTrust = set([n for n in range(1, n+1)])
        for truster, trustee in trust:
            if truster in nonTrust:
                nonTrust.remove(truster)
        if len(nonTrust) != 1:
            return -1
        
        #ensure that everyone trusts last elem in nonTrust
        ans = None
        for judge in nonTrust.copy():
            ans = judge
            for truster, trustee in trust:
                if trustee == judge:
                    nonTrust.add(truster)
        
        return ans if len(nonTrust) == n else -1#bug, returned bool instead of int
        