'''
Problem return min num coins

look for min nums coins to reach 0

base cases:

min number of coins to reach denom is 1
if

brute force

try all possible combination of coins that reach amount, return the one with min coins

f(amount) = 1 + min(f(amount-coin) for coin in coins)
impossible paths should return -1
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0: 0}
        return self.rec(amount, memo, coins)
        

    def rec(self, amount, memo, coins):
        if amount in memo:
            return memo[amount]
        if amount < 0:
            return -1
        
        opts = [self.rec(amount - coin, memo, coins) for coin in coins ]
        opts = list(filter(lambda x: x != -1, opts))


        memo[amount] = (1 + min(opts)) if len(opts) > 0 else -1

        return memo[amount]

        