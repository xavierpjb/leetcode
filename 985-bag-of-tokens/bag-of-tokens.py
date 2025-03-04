class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        #sort then go left till no more power
        # if possible reduce score for power
        score = 0
        maxScore = 0
        tokens.sort()

        l, r = 0, len(tokens) - 1

        while l <= r:
            if tokens[l] <= power:
                score += 1
                maxScore = max(score, maxScore)
                power -= tokens[l]
                l += 1
            elif score > 0:
                score -= 1
                power += tokens[r]
                r -= 1
            else:
                break
            
        return maxScore
        