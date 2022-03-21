'''
partition into as many parts as possible while each char appears at most once
26
input:
    s: string to partition
work:
    find the partition sizes such that the parts appear at most once
output:
    int[]: size of each partition

ideas:
    start with the first char then look for last t = N, s = n
    if the curr chars end is within the range of the curr substring, extend the curr substring
    else restart size

test:

repeating chars
aaababcd
non repeating chars
abcde
'''
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        def createCharEnds(s):
            char_ends = {}
            for i,ch in enumerate(s):
                char_ends[ch] = i
            return char_ends
            
        char_ends = createCharEnds(s)
        
        sizes = []
        start = 0
        end = 0
        for i,ch in enumerate(s):
            if char_ends[ch] > end:
                end = char_ends[ch]
            elif char_ends[ch] == i and char_ends[ch] == end: #two logic bugs, did not properly account for sliding window
                sizes.append(end-start + 1)
                start = i + 1
                end = start
                    
                
        return sizes
            
            
        
        