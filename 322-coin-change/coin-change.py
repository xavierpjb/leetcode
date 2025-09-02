from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        q = deque(coins)
        visited = set()
        level = 1
        lq = len(q)
        while q:
            curr = q.popleft()
            if curr == amount:
                return level
            lq -= 1
            
            if curr < amount and curr not in visited:
                visited.add(curr)

                for nei in [curr + coin for coin in coins]:
                    q.append(nei)

            if lq == 0:
                lq = len(q)
                level += 1
            

        return -1


        