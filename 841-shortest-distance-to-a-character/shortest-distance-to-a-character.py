class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        # pop start
        ans = [len(s)] * len(s)

        closest = float("inf")
        for i in range(len(s)):
            if s[i] == c:
                closest = i
                ans[i] = 0
            elif closest != float("inf"):
                ans[i] = i - closest
        closest = float("inf")
        for i in range(len(s) - 1, -1, -1):
            if s[i] == c:
                closest = i
            elif closest != float("inf"):
                ans[i] = min(ans[i],  closest - i)
        return ans


