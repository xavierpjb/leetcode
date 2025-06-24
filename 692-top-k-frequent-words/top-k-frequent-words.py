'''
Problem: <
examples: 
scenarios:

a,b,a return the 1 most 
a,b

input: list of string
work: find k most frequent strings
output: k most frequent string stored by frequency then lexico

ideas:
creat a map of word to count
turn to list then sort by frequency

create a map of word to count
keep max heap of size k, remove when you find a word less frequenct


'''
from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = defaultdict(int)
        for word in words:
            freq[word] += 1

        class WordFreq:
            def __init__(self, word, count):
                self.word = word
                self.count = count

            def __lt__(self, other):
                if self.count != other.count:
                    return self.count < other.count
                return self.word > other.word
        
        pq = []
        for word, freq in freq.items():
            heapq.heappush(pq, WordFreq(word,freq))
            if len(pq) > k:
                heapq.heappop(pq)

        ans = []  
        for _ in range(k):
            ans.append(heapq.heappop(pq).word)

        ans.reverse()
        return ans







        