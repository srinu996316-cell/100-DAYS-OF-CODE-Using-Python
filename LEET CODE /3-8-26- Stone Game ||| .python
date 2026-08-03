class Solution:
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            best = float("-inf")
            total = 0

            for j in range(i, min(i + 3, n)):
                total += stoneValue[j]
                best = max(best, total - dp[j + 1])

            dp[i] = best

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
        
